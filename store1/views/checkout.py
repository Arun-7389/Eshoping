from django.shortcuts import render, redirect
from django.views import View

from store1.models import Products, Order, Customer
from store1.forms.checkout_forms import CheckoutForm


class Check(View):
    def get(self, request):
        customer_id = request.session.get('customer_id')

        if not customer_id:
            return redirect('login')

        cart = request.session.get('cart', {})
        ids = list(cart.keys())
        products = Products.objects.filter(id__in=ids)
        total = 0
        for product in products:
            quantity = cart.get(str(product.id), 0)
            total += product.price * quantity

        form = CheckoutForm()

        return render(request,'checkout.html',context={ 'products': products,  'cart': cart,  'total': total,     'form': form     }    )

    def post(self, request):
        customer_id = request.session.get('customer_id')
        if not customer_id:
            return redirect('login')

        cart = request.session.get('cart', {})

        form = CheckoutForm(request.POST)

        if form.is_valid():

            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            pincode = form.cleaned_data['pincode']
            phone = form.cleaned_data['phone']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']

            customer = Customer.objects.get(    id=customer_id        )

            products = Products.objects.filter(    id__in=cart.keys()      )

            for product in products:

                quantity = cart.get(str(product.id),0)
                Order.objects.create( customer=customer,   product=product,  price=product.price,
                                      quantity=quantity,   address=address,  city=city, state=state,
                                    pincode=pincode,  phone=phone,latitude=latitude, longitude=longitude   )

            request.session['cart'] = {}

            return redirect('orders')

        # If validation fails,
        # show checkout page again with errors

        products = Products.objects.filter(
            id__in=cart.keys()
        )

        total = 0

        for product in products:

            quantity = cart.get(
                str(product.id),
                0
            )

            total += product.price * quantity

        return render(
            request,
            'checkout.html',
            {
                'products': products,
                'cart': cart,
                'total': total,
                'form': form
            }
        )