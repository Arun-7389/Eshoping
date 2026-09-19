from rest_framework import serializers
from store1.models.orders import Order

class OrderSerializer(serializers.ModelSerializer):

    product_name=serializers.CharField(source='product.name',read_only=True)

    total_price=serializers.SerializerMethodField()

    class Meta:
        model=Order
        fields=['id','product', 'product_name', 'quantity', 'price', 'total_price', 'address','city',
                'state','pincode','phone','latitude','longitude','date', 'status']
        
    def get_total_price(self,obj):
        return obj.price * obj.quantity