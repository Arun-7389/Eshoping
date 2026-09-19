from rest_framework import serializers
from store1.models.Product import Products

class VendorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields="__all__"