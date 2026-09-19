import random 
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.mail import send_mail

from store1.models.Customer import Customer
from store1.models.OTP import PasswordOTP

from django.contrib.auth.hashers import make_password

class CustomerForgotPasswordAPI(APIView):
    def post(self,request):
            
        email=request.data.get('email')
        if not email:
            return Response({'error':'email is required'},status=400)
        customer=Customer.objects.filter(email=email).first()

        if not customer:
            return Response({'error':'Email Not found'},status=404)

        otp=str(random.randint(100000,999999))

        PasswordOTP.objects.filter(email=email,is_verified=False).delete()

        PasswordOTP.objects.create(email=email,otp=otp)

        send_mail(
            'MyStore Password Reset OTP',
            f'Your OTP is {otp}',
            'arunjarpula5@gmail.com',
            [email],
            fail_silently=False
        )
        return Response({'message':'OTP sent successfully'},status=200)


class CustomerVerifyOTPAPI(APIView):
    def post(self,request):

        email=request.data.get('email')
        otp=request.data.get('otp')

        if not email or not otp:
            return Response({'error':'Email and Otp are required'},status=400)
        otp_record= PasswordOTP.objects.filter(email=email,otp=otp,is_verified=False).first()

        if not otp_record:
            return Response({'error':'Invalid OTP'},status=400)
        otp_record.is_verified=True
        otp_record.save()

        return Response({'message':'OTP verified successfully'},status=200)


class CustomerResetPasswordAPI(APIView):

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if not email or not password or not confirm_password:
            return Response( {'error': 'email, password and confirm_password are required'},status=400)

        if password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=400 )

        otp_record = PasswordOTP.objects.filter(email=email, is_verified=True).first()

        if not otp_record:
            return Response({'error': 'OTP verification required'}, status=400 )

        customer = Customer.objects.filter(email=email).first()

        if not customer:
            return Response({'error': 'Customer not found'},status=404 )

        customer.password = make_password(password)
        customer.save()

        PasswordOTP.objects.filter(email=email).delete()

        return Response(
            {'message': 'Password reset successfully'},
            status=200
        )
