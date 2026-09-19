from django.db import models
from .Vendor import Vendor

class Category(models.Model):
    name=models.CharField(max_length=50)
    vendor =models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True,blank=True)

    
    def __str__(self):
        return self.name
