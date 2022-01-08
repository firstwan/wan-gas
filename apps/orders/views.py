import uuid
from datetime import datetime
from rest_framework import viewsets, permissions, status
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import Order
from .serializer import OrderSerializer
from ..products.models import Product

# Create your views here.
class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['transaction_id']
    http_method_names = [ method 
                          for method in viewsets.ModelViewSet.http_method_names 
                          if method not in ['delete']
                        ]

    def create(self, request, *args, **kwargs):
        # Validation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_item_data = request.data.pop('order_items')

        # Extract product id & remove duplicated product id
        product_id_list = [item["product_id"] for item in order_item_data]
        for id in product_id_list:
            if product_id_list.count(id) > 1:
                product_id_list.remove(id)

        # Get Product filter by product id
        product_list = Product.objects.filter(is_active=True) \
                                      .filter(id__in=product_id_list)        

        # Response 400 if a product not found on DB
        if (len(product_list) <= 0 or len(product_list) != len(product_id_list)):
            product_id_not_found = [id for id in product_id_list if id not in [product.id for product in product_list]]
            return Response({'messages': f'Product_id {product_id_not_found} not found.'}, status=status.HTTP_404_NOT_FOUND)       
        else:
            before_discount_price = 0
            promotion_discount_amount = 0
            order_item_list = []

            # Calculate for each order item & order
            for product in product_list:
                total_quantity = sum(item['quantity'] for item in order_item_data if item['product_id'] == product.id)
                if product.qty_in_stock - total_quantity >= 0:
                    new_item = {
                        'product_id': product.id,
                        'quantity': total_quantity,
                        'product_name': product.name,
                        'product_base_price': product.base_price,
                        'discount_amount': 0,
                        'actual_price': product.base_price * total_quantity
                    }
                    order_item_list.append(new_item)

                    before_discount_price += new_item['actual_price']
                    promotion_discount_amount += new_item['discount_amount']
                else:
                    return Response({'messages': f'Product {product.name} quantity insufficient.'}, status=status.HTTP_400_BAD_REQUEST)

            # Start insert order
            order = Order.objects.create(
                            **request.data,
                            transaction_id = self.generate_transaction_id(),
                            before_discount_price = before_discount_price,
                            promotion_discount_amount = promotion_discount_amount,
                            net_price = before_discount_price - promotion_discount_amount,
                            created_by = request.user
                            )
            for order_item in order_item_list:
                order.order_items.create(**order_item)

            headers = self.get_success_headers(serializer.data)
            response_serializer = OrderSerializer(order)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Own defined method
    def generate_transaction_id(self):
        prefix = 'ORD'
        current_date = datetime.today().strftime('%Y%m%d%H%M%S')
        unique_id = str(uuid.uuid4())[:8]

        return prefix + current_date + unique_id.upper()
