from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from store1.models.Product import Products
from store1.models.orders import Order

class VendorDashboard(LoginRequiredMixin,View):

    login_url='vendor_login'

    def get(self,request):

        #Check vendor role
        if not request.user.groups.filter(name='Vendor').exists():
            return redirect('vendor_login')

        vendor=request.user.vendor  # Logged-in vendor

        #vendors products
        products=Products.objects.filter(vendor=vendor)

        #vendors orders
        orders=Order.objects.filter(product__vendor=vendor)

        # Statistics
        total_products = products.count()

        total_orders = orders.count()

        pending_orders=orders.filter(status='Pending').count()

        delivered_orders =orders.filter(status='Delivered').count()

        #Total Sales
        total_sales=sum(order.price*order.quantity for order in orders.filter(status='Delivered'))

        
        return render(request,'vendor_dashboard.html',context={'products':products,
                                    'total_orders':total_orders, 'total_products':total_products,
                                    'pending_orders':pending_orders,'delivered_orders':delivered_orders,'total_sales':total_sales})
