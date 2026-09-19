from rest_framework.views import APIView
from rest_framework.response import Response
from store1.models.Vendor import Vendor
from store1.models.Product import Products
from store1.models.orders import Order

from api.serializers.vendor_Register_serializers import VendorRegisterSerializer
from django.contrib.auth import authenticate,logout

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

class VendorRegisterAPI(APIView):

    def post(self,request):

        serializer =VendorRegisterSerializer(data=request.data)

        if serializer.is_valid():

            vendor =serializer.save()

            return Response({ 'message':'Vendor Registerd successfully',
                            'vendor_id':vendor.id,
                            'username':vendor.user.username,
                            'email':vendor.user.email,
                            'phone':vendor.phone, }  , status=201)
        return Response(serializer.errors,status=400)

#vendor uses Django's User authentication, we can use authenticate()
class VendorLoginAPI(APIView):

    def post(self,request):

        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(request,username=username,password=password)

        if user is None:
            return Response({'error':'Invalid Username or Password'},status=400)

        if not user.groups.filter(name='Vendor').exists():
            return Response({'error':'You Are Not A Vendor'},status=403)

        refresh=RefreshToken.for_user(user)
        refresh['vendor_id'] =user.vendor.id
        refresh['role'] = 'vendor'

        return Response({'message':'Vendor Login Successful',
                         'vendor_id':user.vendor.id,
                         'username':user.username,
                         'email':user.email,
                         'phone':user.vendor.phone,
                         'refresh':str(refresh),
                         'access':str(refresh.access_token)
                         })

class VendorLogoutAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request):

        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error':'Refresh token is required'},status=400)  

        try:
            token = RefreshToken(refresh_token)   
            token.blacklist()
            return Response({'message':'vendor logout successful'})
        except Exception:
            return Response({'error':'Invalid or expired refresh token'},status=400)

class VendorProfileAPI(APIView):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request):

        vendor_id = request.auth['vendor_id']
 
        vendor = Vendor.objects.filter(id=vendor_id).select_related('user').first()

        if not vendor:
            return Response({'error': 'Vendor not found'}, status=404    )

        return Response({
            'vendor_id': vendor.id,
            'username': vendor.user.username,
            'email': vendor.user.email,
            'phone': vendor.phone
        })

class VendorDashboardAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):

        vendor_id= request.auth['vendor_id']

        vendor=Vendor.objects.filter(id=vendor_id).first()

        if not vendor:
            return Response({'error':'vendor not found'},status=404)

        products=Products.objects.filter(vendor=vendor)
        orders=Order.objects.filter(product__vendor=vendor)

        return Response({'vendor_id':vendor.id,
                         'total_products':products.count(),
                         'total_orders':orders.count(),
                         'pending_orders':orders.filter(status='Pending').count(),
                         'processing_orders':orders.filter(status='Processing').count(),
                         'shipped_orders':orders.filter(status='Shipped').count(),
                         'delivered_orders':orders.filter(status='Delivered').count(),
                         'cancelled_orders':orders.filter(status='Cancelled').count()
                         })


