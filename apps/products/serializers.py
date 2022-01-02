from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    base_price = serializers.DecimalField(max_digits=18, decimal_places=4)
    is_active = serializers.NullBooleanField()
    qty_in_stock = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.title)
        instance.base_price = validated_data.get('base_price', instance.code)
        instance.qty_in_stock = validated_data.get('qty_in_stock', instance.linenos)
        # instance.updated_by = validated_data.get('updated_by', instance.linenos)
        instance.updated_date = validated_data.get('updated_date', instance.linenos)
        instance.save()
        return instance