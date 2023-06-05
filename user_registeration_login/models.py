from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
import random

class CustomUser(AbstractUser):
    otp = models.IntegerField(null=True)
    otp_created_at = models.DateTimeField(null=True)

    def generate_otp(self):
        self.otp = random.randint(1000, 9999)
        self.otp_created_at = timezone.now()
        self.username = self.email
        self.save()

    def is_otp_valid(self):
        if self.otp_created_at is None:
            return False
        elif self.otp_created_at + timedelta(minutes=10) < timezone.now():
            return False
        return True
    
    def __str__(self) :
        return f"{self.email}"