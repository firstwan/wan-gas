from rest_framework import serializers
from .models import Order, OrderItem

class OrderListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'product_id': value.product_id,
            'product_name': value.product_name,
            'quantity': value.quantity,
            'product_base_price': value.product_base_price,
            'discount_amount': value.discount_amount,
            'actual_price': value.actual_price
        }

class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.first_name')
    payment_transaction = serializers.ReadOnlyField(source='payment_transaction.transaction_id')
    order_items = OrderListingField(many=True, read_only = True)

    product_id = serializers.CharField(max_length=100)
    # order_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # payment_transaction = serializers.PrimaryKeyRelatedField(queryset=Snippet.objects.all())

    class Meta:
        model = Order
        fields = ['transaction_id', 'before_discount_price', 'promotion_discount_amount', 
                  'net_price', 'created_by', 'created_date', 'order_items', 'buyer', 'payment_transaction']
        read_only_fields = ['transaction_id', 'before_discount_price', 'promotion_discount_amount', 
                            'net_price', 'created_by', 'created_date']
        extra_kwargs = {'buyer_id': {'write_only': True},
                        'product_id': {'write_only': True}}


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product_id', 'product_name', 'quantity', 'product_base_price', 'discount_amount']
        read_only_fields = ['actual_price']
        extra_kwargs = {'product_id': {'write_only': True}}