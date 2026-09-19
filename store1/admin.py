from django.contrib import admin
from .models.Category import Category
from .models.Customer import Customer
from .models.Product import Products
from .models.orders import Order
from .models.Vendor import Vendor
from .models.OTP import PasswordOTP

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','vendor']
    list_filter=['vendor']
    search_fields=['name', 'vendor__user__username']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone']
    search_fields=['first_name','last_name','email','phone']
    ordering=['first_name']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone']
    search_fields = ['user__username','user__email','phone' ]


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','category','vendor']
    list_filter=['category','vendor']
    search_fields=['name','description','category__name','vendor__user__username']
    ordering=['name']

@admin.register(Order)
class Order_Admin(admin.ModelAdmin):
    list_display=['id','product','customer','quantity','price','date','status']
    list_filter=['status','date']
    search_fields=('customer__email','product__name','phone','pincode')
    list_editable=('status',)
    ordering=('-date',)

@admin.register(PasswordOTP)
class PasswordOTPAdmin(admin.ModelAdmin):
    list_display=['id','email','created_at','is_verified']
    list_filter=['created_at','is_verified']
    search_fields=['email']
    ordering=['-created_at']


admin.site.site_header='Mystore Administration'
admin.site.site_title='Mystore Admin'
admin.site.index_title = "MyStore Dashboard"