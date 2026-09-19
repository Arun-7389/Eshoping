from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from store1.models.Product import Products
from api.serializers.product_serializers import ProductSerializer

from api.pagination import MyStorePagination


class ProductListAPI(APIView):



    def get(self,request,): # for seeing all data of products 

        products=Products.objects.all()

        paginator = MyStorePagination()

        page = paginator.paginate_queryset(products, request)

        serializer=ProductSerializer(page,many=True)

        return paginator.get_paginated_response(serializer.data)
    
 
class ProductDetailAPI(APIView):

    def get(self,request,product_id): #for  one produt details  purpose only api/product/1

        product =get_object_or_404(Products,id=product_id)
        serializer=ProductSerializer(product)

        return Response(serializer.data)
  