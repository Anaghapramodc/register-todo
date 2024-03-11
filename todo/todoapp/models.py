from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=15)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    password = models.CharField(max_length=128)  # You may consider using a more secure way to store passwords
    confirm_password = models.CharField(max_length=128)


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
