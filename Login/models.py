from django.db import models
from django import forms


# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=30)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
