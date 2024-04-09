from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from django.contrib.auth.models import User

class MyUser(models.Model):
    username = None   
    email = models.EmailField(primary_key = True, max_length=200)
    USERNAME_FIELD = 'email'
    phone_number = PhoneField(blank=True)
    address = models.CharField( max_length=200)
    name = models.CharField( max_length=100)

    def __str__(self):
        return f'{self.email}'
#phone_number = PhoneField(blank=True, help_text='Contact phone number')


# Create your models here.
