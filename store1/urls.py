
from django.urls import path
from store1.views.home import Index
from store1.views.cart import Cart
from store1.views.signup import Signup
from store1.views.login import Login 
from store1.views.logout import Logout
from store1.views.orders import Orders
from store1.views.checkout import Check
from store1.views.customer_forgot_password import CustomerForgotPassword
from store1.views.customer_verify_otp import CustomerVerifyOTP
from store1.views.customer_reset_password import CustomerResetPassword

from store1.views.vendor_register import VendorSignup
from store1.views.vendor_login import Vendorlogin
from store1.views.vendor_dashboard import VendorDashboard
from store1.views.vendor_Add_product import VendorAddProduct
from store1.views.vendor_category import VendorAddCategory
from store1.views.vendor_edit_product import Vendor_EditProduct
from store1.views.vendor_delete_product import VendorDeleteProduct
from store1.views.vendor_orders_details import VendorOrders_details
from store1.views.vendor_myproduct import MyProduct
from store1.views.vendor_forgot_password import VendorForgotPassword
from store1.views.vendor_verify_otp import VendorVerifyOTP
from store1.views.vendor_reset_password import VendorResetPassword



urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('cart/',Cart.as_view() ,name='cart'),
    path('signup/',Signup.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('orders/',Orders.as_view(),name='orders'),
    path('check/',Check.as_view(),name='checkOut'),
    path('forgot-password/',CustomerForgotPassword.as_view(),name='customer_forgot_password'),
    path('verify-otp/',CustomerVerifyOTP.as_view(),  name='customer_verify_otp'),
    path('reset-password/',CustomerResetPassword.as_view(), name='customer_reset_password'),

    #vendor PAge
    path('vendor/signup/',VendorSignup.as_view(),name='vendor_signup'),
    path('vendor/login/', Vendorlogin.as_view(), name='vendor_login'),
    path('vendor/dashboard/',VendorDashboard.as_view(),name='vendor_dashboard'),
    path('vendor/product/add/',VendorAddProduct.as_view(),name='vendor_add_product'),
    path('vendor/category/add/',VendorAddCategory.as_view(),name='vendor_add_category'),
    path('vendor/product/edit/<int:product_id>/',Vendor_EditProduct.as_view(),name='vendor_edit_product'),
    path('vendor/product/delete/<int:product_id>/',VendorDeleteProduct.as_view(),name='vendor_delete_product'),
    path('vendor/orders/',VendorOrders_details.as_view(),name='vendor_orders_details'),
    path('vendor/myproducts/',MyProduct.as_view(),name='vendor_myproduct'),

    path('vendor/forgot-password/',VendorForgotPassword.as_view(),name='vendor_forgot_password'),
    path('vendor/verify-otp/',VendorVerifyOTP.as_view(),name='vendor_verify_otp'),
    path('vendor/reset-password/',VendorResetPassword.as_view(), name='vendor_reset_password'),

]