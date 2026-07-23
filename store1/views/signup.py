from django.shortcuts import redirect,render

from django.views import View
from store1.forms import CustomerForm
from django.contrib.auth.hashers import make_password

class Signup(View):
    def get(self,request):
        form=CustomerForm()
        return render(request,'signup.html',context={'form':form})
    

    def post(self,request):
        form=CustomerForm(request.POST)
        if form.is_valid():
            customer=form.save(commit=False)
            customer.password=make_password(customer.password)
            customer.save()
            
            return redirect('homepage')
        return render(request,'signup.html',context={'form':form})
    