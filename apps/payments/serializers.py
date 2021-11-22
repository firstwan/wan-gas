from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    payer = serializers.ReadOnlyField(source='payer.first_name')
    payment_method = serializers.ReadOnlyField(source='payment_method.name')

    class Meta:
        model = Payment
        fields = ['id', 'transaction_id', 'payment_type_id', 'payment_type_name', 'amount', 'created_by', 'created_date', 'action_reference_id', 'payer', 'payment_method']
