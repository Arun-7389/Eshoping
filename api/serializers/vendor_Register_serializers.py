from rest_framework import serializers

from django.contrib.auth.models import User,Group
from store1.models.Vendor import Vendor

class VendorRegisterSerializer(serializers.Serializer):

    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)
    phone=serializers.CharField(max_length=10)

    def create(self, validated_data):
        user =User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        vendor=Vendor.objects.create(user=user,phone=validated_data['phone'])

        vendor_group, created =Group.objects.get_or_create(name='Vendor')

        user.groups.add(vendor_group)

        return vendor