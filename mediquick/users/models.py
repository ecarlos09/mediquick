from django.db import models
from django.contrib.auth.models import AbstractUser, Group, User
from django_cryptography.fields import encrypt
import pgcrypto
# from guardian.shortcuts import assign_perm

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = encrypt(models.CharField(max_length=20))
    email = encrypt(models.CharField(max_length=30))
    is_doctor = encrypt(models.BooleanField(default=False))
