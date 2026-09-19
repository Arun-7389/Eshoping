from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password

from store1.models.Customer import Customer
from store1.models.OTP import PasswordOTP


class CustomerResetPassword(View):

    def get(self, request):
        return render(request, 'customer_reset_password.html')

    def post(self, request):

        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        email = request.session.get('reset_email')

        if not email:
            return redirect('customer_forgot_password')

        if password != confirm_password:
            return render(
                request,
                'customer_reset_password.html',
                {'error': 'Passwords do not match'}
            )

        customer = Customer.objects.filter(email=email).first()

        if not customer:
            return redirect('customer_forgot_password')

        customer.password = make_password(password)
        customer.save()

        PasswordOTP.objects.filter(email=email).delete()

        request.session.pop('reset_email', None)

        return redirect('login')