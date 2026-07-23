
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from store1.models.Product import Products
from store1.models.Category import Category


class Index(View):

    def post(self, request):

        product = request.POST.get("product")
        remove = request.POST.get("remove")

        cart = request.session.get("cart", {})

        quantity = cart.get(product)

        if quantity:

            if remove:

                if quantity <= 1:

                    cart.pop(product)

                else:

                    cart[product] -= 1

            else:

                cart[product] += 1

        else:

            cart[product] = 1

        request.session["cart"] = cart

        return redirect(request.META.get("HTTP_REFERER", "homepage"))


    def get(self, request):

        categories = Category.objects.all()

        category = request.GET.get("category")

        search = request.GET.get("search")

        products = Products.objects.all()

        if category:

            products = products.filter(category=category)

        if search:

            products = products.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)|
                Q(category__name__icontains=search)|
                Q(price__icontains=search)
            )

        context = {

            "categories": categories,

            "products": products,

        }

        return render(request, "index.html", context)