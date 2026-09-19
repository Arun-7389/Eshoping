from django.db import models
from .Product import Products
from .Customer import Customer
from django.utils import timezone

class Order(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

    quantity=models.PositiveIntegerField(default=1)

    price=models.DecimalField(max_digits=10,decimal_places=2)

    #devivery details
    address=models.CharField(max_length=250)

    city=models.CharField(max_length=100,blank=True)
    state=models.CharField(max_length=100,blank=True)
    pincode=models.CharField(max_length=6)

    # location for that we need longitude and latitude

    latitude=models.DecimalField(max_digits=10,decimal_places=7,null=True,blank=True)
    longitude =models.DecimalField(max_digits=10,decimal_places=7,blank=True,null=True)

    phone=models.CharField(max_length=12)

    date=models.DateField( default=timezone.now)

    STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),]

    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='Pending')


