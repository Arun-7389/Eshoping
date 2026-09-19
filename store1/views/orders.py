from django.shortcuts import redirect,render
from django.views import View
from store1.models.orders import Order


class Orders(View):

    def get(self,request):

        customer_id=request.session.get('customer_id')

        if not customer_id:
            return redirect('login')

        orders=Order.objects.filter(customer=customer_id).order_by("-date")

        for order in orders:
            order.total_price = order.price * order.quantity

        return render(request,'orders.html',context={'orders':orders})
    
    def post(self,request):
        customer_id=request.session.get('customer_id')

        if not customer_id:
                    return redirect('login')

        order_id = request.POST.get('order_id')

        order=Order.objects.filter(id=order_id,customer=customer_id,status='Pending').first()

        if order:
             order.status='Cancelled'
             order.save()
        return redirect('orders')
