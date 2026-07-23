from django.contrib import admin
from .models.Category import Category
from .models.Customer import Customer
from .models.Product import Products
from .models.orders import Order

# Register your models here.

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)