from django.shortcuts import redirect,render
from django.views import View
from store1.models.orders import Order
from store1.models.Product import Products

class Orders(View):
    def get(self,request):

        print(request.session.items())

        customer_id=request.session.get('customer_id')
        print('Customer ID :' ,customer_id)

        orders=Order.objects.filter(customer=customer_id).order_by("-date")
        print(f'order:{orders}')


        return render(request,'orders.html',context={'orders':orders})