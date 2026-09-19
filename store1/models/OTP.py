from django.db import models
from django.utils import timezone

class PasswordOTP(models.Model):
    email=models.EmailField()
    otp=models.CharField(max_length=6)
    created_at=models.DateTimeField(default=timezone.now)
    is_verified=models.BooleanField(default=False)
