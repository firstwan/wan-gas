from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ['product_id', 'product_name', 'quantity', 'product_base_price', 'discount_amount', 'actual_price']
        read_only_fields = ['product_name', 'product_base_price', 'discount_amount', 'actual_price']


class OrderSerializer(serializers.ModelSerializer):
    shop_id = serializers.IntegerField(write_only=True)
    buyer = serializers.ReadOnlyField(source='buyer.first_name')
    payment_transaction = serializers.ReadOnlyField(source='payment_transaction.transaction_id')
    order_items = OrderItemSerializer(many=True, required=True)

    # order_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # payment_transaction = serializers.PrimaryKeyRelatedField(queryset=Snippet.objects.all())

    # Magic binding to order items
    def validate_order_items(self, attrs):
        if len(attrs) == 0:
            raise serializers.ValidationError('Required at least one order item.')
        return attrs

    class Meta:
        model = Order
        fields = ['shop_id', 'transaction_id', 'before_discount_price', 'promotion_discount_amount', 
                  'net_price', 'created_by', 'created_date', 'order_items', 'buyer', 'payment_transaction']
        read_only_fields = ['transaction_id', 'before_discount_price', 'promotion_discount_amount', 
                            'net_price', 'created_by', 'created_date', 'buyer', 'payment_transaction']
