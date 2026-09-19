from django.db import models
from .Category import Category
from .Vendor import Vendor

class Products(models.Model):
    name=models.CharField(max_length=60)
    price=models.FloatField(default=0)

    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    description=models.CharField(max_length=300,blank=True,null=True)

    image=models.ImageField(upload_to='uploads/Product')

    vendor =models.ForeignKey(Vendor,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name

