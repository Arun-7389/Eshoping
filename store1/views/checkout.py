from django.shortcuts import render,redirect
from django.views import View
from store1.models import Products,Order,Customer

class Check(View):
    def get(self,request):
        cart=request.session.get('cart',{})
        ids=list(cart.keys())

        products=Products.objects.filter(id__in=ids)
        total=0

        for product in products:
            quantity = cart.get(str(product.id))
            total+=product.price*quantity

        return render(request,'checkout.html',context={'products':products,'cart':cart,'total':total})
    
    def post(self,request):

        address =request.POST.get('address')
        phone = request.POST.get('phone')

        customer =request.session.get('customer_id')

        cart = request.session.get('cart',{})

        products =Products.objects.filter(id__in=cart.keys())

        for product in products:
            order=Order(
                customer=Customer.objects.get(id=customer),
                product=product,

                price=product.price,

                quantity= cart.get(str(product.id)),

                address=address,

                phone=phone
            )
            order.save()
        request.session['cart']={}      

        return redirect('orders')