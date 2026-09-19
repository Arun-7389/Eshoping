from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    def __str__(self):
        return self.user.username