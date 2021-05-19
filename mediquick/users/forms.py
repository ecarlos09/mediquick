from .models import CustomUser
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):
    error_css_class = 'error'
    required_css_class = 'required'
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']