from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'address1', 'address2', 'address_postcode', 'address_city', 'address_state', 'owner_id', 'nickname']