from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.unique_id')
    owner_id = serializers.IntegerField()

    class Meta:
        model = Shop
        fields = ['name', 'address1', 'address_postcode', 'address_city', 'address_state', 'owner_id', 'owner']
        read_only_fields = ['id','address2', 'nickname']
        extra_kwargs = {'owner_id': {'write_only': True}}
