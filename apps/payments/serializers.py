from rest_framework import serializers
from .models import Payment, PaymentMethod
from ..customers.models import Customer

class PaymentSerializer(serializers.ModelSerializer):
    payer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), write_only=True)
    payment_method_id = serializers.PrimaryKeyRelatedField(queryset=PaymentMethod.objects.all(), write_only=True)
    payer = serializers.ReadOnlyField(source='payer.first_name')
    payment_method = serializers.ReadOnlyField(source='payment_method.name')
    payment_type_id = serializers.ChoiceField(choices=Payment.PaymentType)

    class Meta:
        model = Payment
        fields = ['id', 'transaction_id', 'payment_type_id', 'amount', 'payment_status_id', 'created_by', 
                    'created_date', 'action_reference_id', 'payer_id', 'payment_method_id', 'payer', 'payment_method']
        read_only_fields = ['id', 'transaction_id', 'created_by', 'created_date']

    def create(self, validated_data):
        customer_obj = validated_data.pop('payer_id')
        payment_method_obj = validated_data.pop('payment_method_id')
        return Payment.objects.create(**validated_data, 
                        payment_type_name=validated_data['payment_type_id'].label,
                        payment_status_name = validated_data['payment_status_id'].label,
                        payer = customer_obj,
                        payment_method = payment_method_obj)

    def update(self, instance, validated_data):
        instance.payment_type_name=validated_data['payment_type_id'].label
        instance.payment_status_name=validated_data['payment_status_id'].label
        instance.save()
        return instance