from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from store1.models.Product import Products

class MyProduct(LoginRequiredMixin,ListView):

    model=Products
    template_name='vendor_myproduct.html'
    context_object_name='products'
    login_url='vendor_login'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Vendor').exists():
            return redirect('vendor_login')

        return super().dispatch(request, *args, **kwargs)
    def get_queryset(self):

        return Products.objects.filter(
            vendor=self.request.user.vendor
        )

    