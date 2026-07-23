from django.shortcuts import render,redirect

from django.views import View

from store1.models.Product import Products
from store1.models.Category import Category


class Cart(View):
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')

        cart=request.session.get('cart',{})

        quantity=cart.get(product)

        if quantity:
            if remove:
                if quantity<=1:
                    cart.pop(product)
                else:
                    cart[product]=quantity-1
            else:
                cart[product]=quantity+1
        request.session['cart']=cart
        return redirect('cart')


    def get(self,request):

        cart=request.session.get('cart',{})

        ids=[ int(i) for i in cart.keys() if str(i).isdigit()]

        products=Products.objects.filter(id__in=ids)

        categories=Category.objects.all()
       

        return render(request,'cart.html',context={'products':products,'categories':categories})