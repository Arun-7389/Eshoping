from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from store1.forms.vendor_category_forms import VendorCategoryForm


class VendorAddCategory(LoginRequiredMixin, View):

    login_url = 'vendor_login'

    def get(self, request):

        if not request.user.groups.filter(name='Vendor').exists():
            return redirect('vendor_login')

        form = VendorCategoryForm()

        return render(request, 'vendor_add_category.html', {
            'form': form
        })

    def post(self, request):

        if not request.user.groups.filter(name='Vendor').exists():
            return redirect('vendor_login')

        form = VendorCategoryForm(request.POST)

        if form.is_valid():

            category = form.save(commit=False)

            category.vendor = request.user.vendor

            category.save()

            return redirect('vendor_add_product')

        return render(request, 'vendor_add_category.html', {
            'form': form
        })