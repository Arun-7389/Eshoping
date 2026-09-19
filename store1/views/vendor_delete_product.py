from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView

from store1.models.Product import Products
from django.urls import reverse_lazy
class VendorDeleteProduct(LoginRequiredMixin,DeleteView):
    model=Products
    template_name='vendor_delete_product.html'

    pk_url_kwarg='product_id'
    login_url='vendor_login'

    success_url = reverse_lazy('vendor_dashboard')

    def dispatch(self, request, *args, **kwargs):

        if not request.user.groups.filter(name='Vendor').exists():# this is for checking vendor is logined or not 
            return redirect('vendor_login')

        if not request.user.has_perm('store1.delete_products'):
            return redirect('vendor_login')
    
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self): #Vendor A cannot delete Vendor B's product.
        return Products.objects.filter(vendor=self.request.user.vendor)
    # def get_success_url(self):
    #     return '/vendor/dashboard/'
    