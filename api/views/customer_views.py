from rest_framework.views import APIView #register api
from rest_framework.response import Response
from api.serializers.customer_serializers import CustomerSerializer

#login Api 
from store1.models.Customer import Customer
from django.contrib.auth.hashers import check_password

#JWT TOKEN 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from api.authentication import CustomerJWTAuthentication

class CustomerRegisterAPI(APIView):
   
    def post(self,request):

        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=201)
        
        return Response(serializer.errors,status=400)

    
class CutomerLoginAPI(APIView):

    def post(self, request):

        email=request.data.get('email')
        password=request.data.get('password')

       

        customer=Customer.objects.filter(  email=email).first()

        if customer is None:
            return Response({'error':'Invalid Email or password'},status=400)

        if not check_password(password,customer.password):
            return Response({'error':'Invalid Email or password'},status=400)

        refresh=RefreshToken()
        refresh['customer_id']=customer.id
        refresh['role']='customer'
       
        return Response({'message':'Login successful',
                         'customer_id':customer.id,
                         'email':customer.email,
                         'first_name':customer.first_name,
                         'refresh': str(refresh),
                         'access': str(refresh.access_token)
                         })


class CustomerLogoutAPI(APIView):
    authentication_classes=[CustomerJWTAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self,request):

        refresh_token=request.data.get('refresh')

        if not refresh_token:
            return Response({'error':'Refresh token is required'},status=400)
        try:
            token=RefreshToken(refresh_token)
            token.blacklist()

            return Response({'message':'Customer logout successful'})
        
        except Exception:

            return Response({'error':'Invalid or expired refresh token '},status=400)


class CustomerProfileAPI(APIView):

    authentication_classes=[CustomerJWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):

        customer_id= request.auth['customer_id']

        customer =Customer.objects.filter(id=customer_id).first()

        if not customer:
            
            return Response({'error':'customer not found'},status=404)

        return Response({'id':customer.id,
                         'first_name':customer.first_name,
                         'last_name':customer.last_name,
                         'phone':customer.phone,
                         'email':customer.email,
                         })


class CustomerProfileUpdateAPI(APIView):

    authentication_classes=[CustomerJWTAuthentication]
    permission_classes=[IsAuthenticated]
    def put(self,request):
        customer_id= request.auth['customer_id']
       
        customer=Customer.objects.filter(id=customer_id).first()

        if not customer:
            return Response({'error':'Customer Not Found '},status=400)

        customer.first_name=request.data.get('first_name',customer.first_name)
        customer.last_name=request.data.get('last_name',customer.last_name)
        customer.phone=request.data.get('phone',customer.phone)
        customer.save()

        return Response({
            'message':'Profile updated successfully',
            'customer_id':customer.id,
            'first_name':customer.first_name,
            'last_name':customer.last_name,
            'phone':customer.phone,
            'email':customer.email
        })


        