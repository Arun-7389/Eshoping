import random

from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from store1.models.OTP import PasswordOTP


# Vendor Forgot Password
class VendorForgotPasswordAPI(APIView):

    def post(self, request):

        email = request.data.get('email')

        if not email:
            return Response(
                {'error': 'email is required'},
                status=400
            )

        user = User.objects.filter(
            email=email,
            groups__name='Vendor'
        ).first()

        if not user:
            return Response(
                {'error': 'Vendor email not found'},
                status=404
            )

        otp = str(random.randint(100000, 999999))

        PasswordOTP.objects.filter(
            email=email,
            is_verified=False
        ).delete()

        PasswordOTP.objects.create(
            email=email,
            otp=otp
        )

        send_mail(
            'MyStore Vendor Password Reset OTP',
            f'Your OTP is {otp}',
            'arunjarpula5@gmail.com',
            [email],
            fail_silently=False
        )

        return Response(
            {'message': 'OTP sent successfully'},
            status=200
        )


# Vendor Verify OTP
class VendorVerifyOTPAPI(APIView):

    def post(self, request):

        email = request.data.get('email')
        otp = request.data.get('otp')

        if not email or not otp:
            return Response(
                {'error': 'Email and OTP are required'},
                status=400
            )

        otp_record = PasswordOTP.objects.filter(
            email=email,
            otp=otp,
            is_verified=False
        ).first()

        if not otp_record:
            return Response(
                {'error': 'Invalid OTP'},
                status=400
            )

        otp_record.is_verified = True
        otp_record.save()

        return Response(
            {'message': 'OTP verified successfully'},
            status=200
        )


# Vendor Reset Password
class VendorResetPasswordAPI(APIView):

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if not email or not password or not confirm_password:
            return Response(
                {
                    'error':
                    'email, password and confirm_password are required'
                },
                status=400
            )

        if password != confirm_password:
            return Response(
                {'error': 'Passwords do not match'},
                status=400
            )

        otp_record = PasswordOTP.objects.filter(
            email=email,
            is_verified=True
        ).first()

        if not otp_record:
            return Response(
                {'error': 'OTP verification required'},
                status=400
            )

        user = User.objects.filter(
            email=email,
            groups__name='Vendor'
        ).first()

        if not user:
            return Response(
                {'error': 'Vendor not found'},
                status=404
            )

        user.password = make_password(password)
        user.save()

        PasswordOTP.objects.filter(
            email=email
        ).delete()

        return Response(
            {'message': 'Password reset successfully'},
            status=200
        )