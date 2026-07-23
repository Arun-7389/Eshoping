from django.shortcuts import render,redirect
from store1.models.Customer import Customer
from django.views import View
from django.contrib.auth.hashers import check_password

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.objects.filter(email=email).first()

        if customer:
            if check_password(password,customer.password):
                request.session['customer_id']=customer.id
                request.session['customer_name']=customer.first_name

                return redirect('homepage')
        return render(request,'login.html',{'error':'Invalid Password or Email'})