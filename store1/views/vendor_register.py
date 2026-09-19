from django.shortcuts import redirect,render
from django.views import View
from django.contrib.auth.models import Group,User

from store1.models.Vendor import Vendor
from store1.forms.Vendor_forms import VendorForm

class VendorSignup(View):
    def get(self,request):
        form=VendorForm()
        return render(request,'vendor_signup.html',context={'form':form})
    def post(self,request):
        form=VendorForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            vendor=Vendor.objects.create(user=user,phone=form.cleaned_data['phone'])

            vender_group,created=Group.objects.get_or_create(name='Vendor')

            user.groups.add(vender_group)
            return redirect('vendor_login')
        return render(request,'vendor_signup.html',context={'form':form})