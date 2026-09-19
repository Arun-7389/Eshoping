import random

from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.models import User

from store1.models.OTP import PasswordOTP


class VendorForgotPassword(View):

    def get(self, request):
        return render(request, 'vendor_forgot_password.html')

    def post(self, request):

        email = request.POST.get('email')

        user = User.objects.filter(
            email=email,
            groups__name='Vendor'
        ).first()

        if not user:
            return render(
                request,
                'vendor_forgot_password.html',
                {'error': 'Vendor email not found'}
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

        request.session['vendor_reset_email'] = email

        return redirect('vendor_verify_otp')