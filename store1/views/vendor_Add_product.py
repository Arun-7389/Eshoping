from django.shortcuts import redirect,render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from store1.forms.vendor_product_forms import VendorProductForm

class VendorAddProduct(LoginRequiredMixin,View):
    login_url = 'vendor_login'

    def get(self,request):
        if not request.user.groups.filter(name='Vendor').exists():
            return redirect('vendor_login')

        form= VendorProductForm()

        return render(request,'vendor_add_product.html',context={'form':form})
    
    def post(self,request):

        if not request.user.groups.filter(name='Vendor').exists():
            return redirect('vendor_login')
        
        if not request.user.has_perm('store1.add_products'):
            return redirect('vendor_login')
        
        form=VendorProductForm(request.POST,request.FILES)

        if form.is_valid():

            product=form.save(commit=False)

            product.vendor=request.user.vendor

            product.save()

            return redirect('vendor_dashboard')
        return render(request,'vendor_add_product.html',context={'form':form})




