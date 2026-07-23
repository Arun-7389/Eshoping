from django.db import models
from .Product import Products
from .Customer import Customer
from django.utils import timezone
class Order(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    address=models.CharField(max_length=250)
    phone=models.CharField(max_length=12)

    date=models.DateField( default=timezone.now)

    status=models.BooleanField(default=False)


