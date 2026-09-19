from django.shortcuts import render,redirect
from store1.models.Customer import Customer
from django.views import View
from django.contrib.auth.hashers import check_password
from store1.forms.login_forms import LoginForm

class Login(View):
    def get(self,request):

        form=LoginForm()
        return render(request,'login.html',context={'form':form})
    
    def post(self,request):

        form =LoginForm(request.POST)

        if form.is_valid():
             
             email=form.cleaned_data['email']
             password=form.cleaned_data['password']

             customer=Customer.objects.filter(email=email).first()

             if customer and check_password(password,customer.password):
                    
                    request.session['customer_id']=customer.id
                    request.session['customer_name']=customer.first_name
                    return redirect('homepage')
                
             form.add_error(None,"Invalid email or password")
             
        return render(request,'login.html',context={'form':form})