from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.views import View
from django.contrib.auth.models import User

class Vendorlogin(View):
    def get(self,request):
        return render(request,'vendor_login.html')

    def post(self,request):

        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(request,username=username,password=password)

        if user is not None:
            if user.groups.filter(name='Vendor').exists():
                login(request,user)
                return redirect('vendor_dashboard')
        return render(request,'vendor_login.html',{'error':'invalid user name or password'})