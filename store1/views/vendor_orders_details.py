from django.shortcuts import redirect,render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from store1.models.orders import Order

class VendorOrders_details(LoginRequiredMixin,View):
    login_url='vendor_login'
    def get(self,request):

        if not request.user.groups.filter(name='Vendor').exists():
            return redirect('vendor_login')

        if not request.user.has_perm('store1.view_order'):
              return redirect('vendor_login')
        
        orders=Order.objects.filter(product__vendor=request.user.vendor).order_by('-date')

        return render(request,'vendor_orders_details.html',context={'orders':orders})
    
    def post(self,request):

        if not request.user.groups.filter(name='Vendor').exists():
                    return redirect('vendor_login')
        
        if not request.user.has_perm('store1.change_order'):
              return redirect('vendor_login')

        order_id = request.POST.get('order_id')
        new_status = request.POST.get('status')

        order=Order.objects.filter(id=order_id,product__vendor=request.user.vendor).first()

        allowed_transitions={
              'Pending':'Processing',
              'Processing':'Shipped',
              'Shipped':'Delivered'

        }

        if order and allowed_transitions.get(order.status)== new_status:
              order.status = new_status
              order.save()
        return redirect('vendor_orders_details')
