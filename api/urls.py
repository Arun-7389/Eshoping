from django.urls import path

from .views.product_view import ProductListAPI,ProductDetailAPI
from .views.customer_views import CustomerRegisterAPI,CutomerLoginAPI,CustomerLogoutAPI,CustomerProfileAPI,CustomerProfileUpdateAPI
from .views.order_view import CustomerOrderListAPI,CustomerOrderDetailAPI
from .views.cart_view import CustomerCartAPI,CustomerCartAddAPI,CustomerCartRemoveAPI
from .views.checkout_view import CustomerCheckoutAPI
from .views.customer_forgot_password_API import CustomerForgotPasswordAPI,CustomerVerifyOTPAPI,CustomerResetPasswordAPI

from .views.vendor_view import VendorRegisterAPI,VendorLoginAPI,VendorLogoutAPI,VendorProfileAPI,VendorDashboardAPI
from .views.vendor_category_view import VendorCategoryCreateAPI
from .views.vendor_product_view import VendorProductCreateAPI,VendorProductListAPI,VendorProductUpdateAPI,VendorProductDeleteAPI
from .views.vendor_orders_view import VendorOrderListAPI
from .views.vendor_forgot_password_API import VendorForgotPasswordAPI,VendorVerifyOTPAPI, VendorResetPasswordAPI


urlpatterns=[
    path('products/',ProductListAPI.as_view(),name='api_products'),
    path('products/<int:product_id>/',ProductDetailAPI.as_view(),name='api_product_detail'),

    path('customer/register/',CustomerRegisterAPI.as_view(),name='customer_register'),
    path('customer/login/',CutomerLoginAPI.as_view(),name='customer_login'),
    path('customer/logout/',CustomerLogoutAPI.as_view(),name='customer_logout'),
    path('customer/profile/',CustomerProfileAPI.as_view(),name='customer_profile'),
    path('customer/profile/update/',CustomerProfileUpdateAPI.as_view(),name='customer_profile_update'),

    path('customer/orders/',CustomerOrderListAPI.as_view()),
    path('customer/orders/<int:order_id>/',CustomerOrderDetailAPI.as_view(),name='customer_order_detail'),

    path('customer/cart/',CustomerCartAPI.as_view(),name='customer_cart'),
    path('customer/cart/add/',CustomerCartAddAPI.as_view(),name='customer_cart_add'),
    path('customer/cart/remove/',CustomerCartRemoveAPI.as_view(),name='customer_cart_remove'),


    path('customer/checkout/',CustomerCheckoutAPI.as_view(),name='customer_checkout'),

    #password verification forgotpassword
    path('customer/forgot-password/',CustomerForgotPasswordAPI.as_view(),name='customer_forgot_password_api'),
    path('customer/verify-otp/',CustomerVerifyOTPAPI.as_view(),name='customer_verify_otp_api'),
    path('customer/reset-password/',CustomerResetPasswordAPI.as_view(),name='customer_reset_password_api'),


    #Vendor ApI
    path('vendor/register/',VendorRegisterAPI.as_view(),name='vendor_register'),
    path('vendor/login/',VendorLoginAPI.as_view(),name='vendor_login_api'),
    path('vendor/logout/',VendorLogoutAPI.as_view(),name='vendor_logout_api'),
    path('vendor/profile/',VendorProfileAPI.as_view(),name='vendor_profile'),

    path('vendor/category/',VendorCategoryCreateAPI.as_view(),name='vendor_category'),
    path('vendor/product/',VendorProductCreateAPI.as_view(),name='vendor_product'),
    path('vendor/products/',VendorProductListAPI.as_view(),name='vendor_products'),
    path('vendor/product/<int:product_id>/',VendorProductUpdateAPI.as_view(),name='vendor_product_update'),
    path('vendor/product/<int:product_id>/delete/',VendorProductDeleteAPI.as_view(),name='vendor_product_delete'),
    path('vendor/orders/',VendorOrderListAPI.as_view(),name='vendor_order_list'),
    path('vendor/dashboard/',VendorDashboardAPI.as_view(),name='vendor_dashboard_api'),



    path('vendor/forgot-password/', VendorForgotPasswordAPI.as_view(), name='vendor_forgot_password_api'),
    path('vendor/verify-otp/',VendorVerifyOTPAPI.as_view(), name='vendor_verify_otp_api'),
    path('vendor/reset-password/', VendorResetPasswordAPI.as_view(),name='vendor_reset_password_api'),

]