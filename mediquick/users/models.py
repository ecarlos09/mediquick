from django.db import models
from django.contrib.auth.models import AbstractUser, Group, User
# from django_cryptography.fields import encrypt
# import pgcrypto

# Create your models here.

# class CustomUser(AbstractUser):
#     name = encrypt(models.CharField(max_length=20))
#     email = encrypt(models.CharField(max_length=30))
#     is_doctor = encrypt(models.BooleanField(default=False))

class CustomUser(AbstractUser):
    name = (models.CharField(max_length=20))
    email = (models.CharField(max_length=30))
    is_doctor = (models.BooleanField(default=False))