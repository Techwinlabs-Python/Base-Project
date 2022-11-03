from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    email = models.EmailField(verbose_name='email address',\
                max_length=255, unique=True)
    phone = models.CharField(max_length=10, null=True)
    gender = models.CharField(choices=choices, max_length=10, null=True)
