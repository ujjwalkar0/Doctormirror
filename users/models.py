from django.db import models

# Create your models here.

class users(models.Model):
    firstname=models.Charfield(max_len=20)
    lastname=models.Charfield(max_len=20)
    email_id=models.EmailField(max_length=254)
    password1=models.CharField(max_length=32, widget=models.PasswordInput)
    password2=models.CharField(max_length=32, widget=models.PasswordInput)
    