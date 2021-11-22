from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.first_name')
    payment_transaction = serializers.ReadOnlyField(source='payment_transaction.transaction_id')
    # payment_transaction = serializers.PrimaryKeyRelatedField(queryset=Snippet.objects.all())

    class Meta:
        model = Order
        fields = ['transaction_id', 'before_discount_price', 'promotion_discount_amount', 'net_price', 'created_by', 'created_date', 'buyer', 'payment_transaction']
