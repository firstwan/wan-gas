from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.unique_id')
    owner_id = serializers.IntegerField()

    class Meta:
        model = Shop
        fields = ['id', 'name', 'address1', 'address_postcode', 'address_city', 'address_state', 'owner_id', 'owner']
        read_only_fields = ['address2', 'nickname']
