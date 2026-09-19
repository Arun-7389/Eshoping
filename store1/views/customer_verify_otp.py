from django.shortcuts import render, redirect
from django.views import View

from store1.models.OTP import PasswordOTP


class CustomerVerifyOTP(View):

    def get(self, request):
        return render(request, 'customer_verify_otp.html')

    def post(self, request):

        otp = request.POST.get('otp')
        email = request.session.get('reset_email')

        if not email:
            return redirect('customer_forgot_password')

        otp_record = PasswordOTP.objects.filter(
            email=email,
            otp=otp,
            is_verified=False
        ).first()

        if not otp_record:
            return render(
                request,
                'customer_verify_otp.html',
                {'error': 'Invalid OTP'}
            )

        otp_record.is_verified = True
        otp_record.save()

        return redirect('customer_reset_password')