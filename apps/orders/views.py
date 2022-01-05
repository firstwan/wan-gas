from rest_framework import viewsets, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializer import OrderSerializer, OrderItemSerializer
import uuid
from datetime import datetime
from ..products.models import Product

# Create your views here.
class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = [ method 
                          for method in viewsets.ModelViewSet.http_method_names 
                          if method not in ['delete']
                        ]

    def create(self, request, *args, **kwargs):
        # Validation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_item_data = request.data.pop('order_items')

        # Get Product
        product_id_list = [item["product_id"] for item in order_item_data]
        product_list = Product.objects.filter(id__in=product_id_list)
        order_item_list = []

        before_discount_price = 0
        promotion_discount_amount = 0
        net_price = 0

        if (len(product_list) > 0):
            # Calculate for each order item & order
            for product in product_list:
                request_order_item = next((p for p in order_item_data if p['product_id'] == product.id), None)
                new_item = {
                    'product_id': product.id,
                    'quantity': request_order_item['quantity'],
                    'product_name': product.name,
                    'product_base_price': product.base_price,
                    'discount_amount': 0,
                    'actual_price': product.base_price
                }
                order_item_list.append(new_item)

                before_discount_price += product.base_price
                promotion_discount_amount += 0
                net_price += product.base_price - 0

            # Start insert order
            order = Order.objects.create(
                            **request.data,
                            transaction_id = self.generate_transaction_id(),
                            before_discount_price = before_discount_price,
                            promotion_discount_amount = promotion_discount_amount,
                            net_price = net_price,
                            created_by = request.user
                            )
            for order_item in order_item_list:
                order.order_items.create(**order_item)

            headers = self.get_success_headers(serializer.data)
            response_serializer = OrderSerializer(order)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'messages': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)       


    # Own defined method
    def generate_transaction_id(self):
        prefix = 'ORD'
        current_date = datetime.today().strftime('%Y%m%d%H%M%S')
        unique_id = str(uuid.uuid4())[:8]

        return prefix + current_date + unique_id.upper()
