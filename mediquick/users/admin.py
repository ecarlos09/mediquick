from django.contrib import admin

# Register your models here.

#do we need this?????
from .models import CustomUser

admin.site.register(CustomUser)