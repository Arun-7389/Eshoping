from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from store1.models.OTP import PasswordOTP


class VendorResetPassword(View):

    def get(self, request):
        return render(request, 'vendor_reset_password.html')

    def post(self, request):

        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        email = request.session.get('vendor_reset_email')

        if not email:
            return redirect('vendor_forgot_password')

        if password != confirm_password:
            return render(
                request,
                'vendor_reset_password.html',
                {'error': 'Passwords do not match'}
            )

        user = User.objects.filter(
            email=email,
            groups__name='Vendor'
        ).first()

        if not user:
            return redirect('vendor_forgot_password')

        user.password = make_password(password)
        user.save()

        PasswordOTP.objects.filter(email=email).delete()

        request.session.pop('vendor_reset_email', None)

        return redirect('vendor_login')