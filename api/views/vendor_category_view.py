from rest_framework.views import APIView
from rest_framework.response import Response

from store1.models.Category import Category
from store1.models.Vendor import Vendor

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class VendorCategoryCreateAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request):

        vendor_id=request.auth['vendor_id']

        name=request.data.get('name')

     
        if not name:
            return Response({'error':'Category Name is Required'},status=400)

        vendor = Vendor.objects.filter(id=vendor_id).first()
        
        if not vendor:
            return Response({'error':'Vendor not found'},status=404)

        category=Category.objects.create(name=name,vendor=vendor)

        return Response({'message':'category created successfully',
                         'category_id':category.id, 'name':category.name,
                         'vendor_id':vendor.id},status=201)