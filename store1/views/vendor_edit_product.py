from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from store1.models.Product import Products
from store1.forms.vendor_product_forms import VendorProductForm

class Vendor_EditProduct(LoginRequiredMixin,UpdateView):

    model = Products
    form_class = VendorProductForm
    template_name = 'vendor_edit_product.html'

    pk_url_kwarg = 'product_id'
    login_url = 'vendor_login'

    success_url=reverse_lazy('vendor_dashboard') # this is for rediricting in cbv

    def dispatch(self, request, *args, **kwargs):# this is for checking vendor is logined or not 

        if not request.user.groups.filter(name ='Vendor').exists():
            return redirect('vendor_login')
        
        if not request.user.has_perm('store1.change_products'):#Permission   Can this user edit products?
            return redirect('vendor_login')
        
        return super().dispatch(request,*args,**kwargs)
    
    def get_queryset(self): #its cheking ownership Vendor A cannot edit Vendor B's product.
        return Products.objects.filter(
            vendor=self.request.user.vendor)   # Ownership Can this user edit THIS particular product?
    # def get_success_url(self):
    #     return '/vendor/dashboard/' without hard coding we are doing reverse_lazy on succesful url

