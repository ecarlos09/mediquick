from django.db import models
from django.contrib.auth.models import AbstractUser, Group, User
from django_cryptography.fields import encrypt
# from guardian.shortcuts import assign_perm

# Create your models here.
class CustomUsers(models.Model):
    # user type
    user_type = models.CharField(User, on_delete=models.CASCADE)
    # username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = encrypt(models.CharField(max_length=50))
    email = models.CharField(max_length=30, blank=True)

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)

class Patient(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # continue with normal properties
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = encrypt(models.CharField(max_length=50))
    email = models.CharField(max_length=30, blank=True)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        permissions = (
            ('doctor_home', 'Doctor homepage'),
        )

# company_a = Company.objects.create(name="Company A")
# company_b = Company.objects.create(name="Company B")
# # create groups
# company_user_group_a = Group.objects.create(name="Company User Group A")
# company_user_group_b = Group.objects.create(name="Company User Group B")
# # assign object specific permissions to groups
# assign_perm('change_company', company_user_group_a, company_a)
# assign_perm('change_company', company_user_group_b, company_b)