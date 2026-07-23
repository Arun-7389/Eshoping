from django.contrib import admin
from django.urls import path
from store1.views.home import Index
from store1.views.cart import Cart
from store1.views.signup import Signup
from store1.views.login import Login 
from store1.views.logout import Logout
from store1.views.orders import Orders
from store1.views.checkout import Check


urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('cart/',Cart.as_view() ,name='cart'),
    path('signup/',Signup.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('orders/',Orders.as_view(),name='orders'),
    path('check/',Check.as_view(),name='checkOut')

]