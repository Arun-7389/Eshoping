from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from store1.models.Vendor import Vendor
from api.serializers.vendor_product_serializers import VendorProductSerializer

from store1.models.Product import Products
from api.pagination import MyStorePagination


class VendorProductCreateAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request):

        vendor_id=request.auth['vendor_id']

        vendor =Vendor.objects.filter(id=vendor_id).first()

        if not vendor:
            return Response({'error':'Vendor not found'},status=404)

        data = request.data.copy()
        data['vendor']=vendor.id

        serializer =VendorProductSerializer(data=data)

        if serializer.is_valid():
            product =serializer.save()

            return Response({'message':'Product added   successfully',
                             'product':VendorProductSerializer(product).data},status=201)

        return Response(serializer.errors,status=400)

class VendorProductListAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
         vendor_id=request.auth['vendor_id']

         products =Products.objects.filter(vendor_id=vendor_id)

         paginator =MyStorePagination()

         page = paginator.paginate_queryset(products,request)

         serializer = VendorProductSerializer(page,many=True)

         return paginator.get_paginated_response(serializer.data)

class VendorProductUpdateAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def put(self,request,product_id):

        vendor_id=request.auth['vendor_id']

        product =Products.objects.filter(id=product_id,vendor_id=vendor_id).first()

        if not product:
            return Response({'error':'product not found '},status=400)

        serializer = VendorProductSerializer(product,data=request.data,partial=True)

        if serializer.is_valid():
            product=serializer.save()

            return Response({'message':'product Updated Successfully','product':VendorProductSerializer(product).data})
        return Response(serializer.errors,status=400)

class VendorProductDeleteAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def delete(self,request,product_id):
        vendor_id=request.auth['vendor_id']

        product= Products.objects.filter(id=product_id,vendor_id=vendor_id).first()

        if not product:
            return Response({'error':'Product not Found'},status=400)

        product.delete()
        return Response({'message':'Product delete  successfully'})
