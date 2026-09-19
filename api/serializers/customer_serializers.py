from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from store1.models.Customer import Customer

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model= Customer
        fields ='__all__'
    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])

        return Customer.objects.create(**validated_data)