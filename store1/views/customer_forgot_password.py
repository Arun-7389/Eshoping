import random

from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail

from store1.models.Customer import Customer
from store1.models.OTP import PasswordOTP


class CustomerForgotPassword(View):

    def get(self, request):
        return render(request, 'customer_forgot_password.html')

    def post(self, request):

        email = request.POST.get('email')

        customer = Customer.objects.filter(email=email).first()

        if not customer:
            return render( request,'customer_forgot_password.html',context= {'error': 'Email not found'} )

        otp = str(random.randint(100000, 999999))

        PasswordOTP.objects.filter( email=email, is_verified=False ).delete()

        PasswordOTP.objects.create(
            email=email,
            otp=otp
        )

        send_mail(
            'MyStore Password Reset OTP',
            f'Your OTP is {otp}',
            'arunjarpula5@gmail.com',
            [email],
            fail_silently=False
        )

        request.session['reset_email'] = email

        return redirect('customer_verify_otp')