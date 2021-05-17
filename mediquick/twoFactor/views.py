from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from .models import Profile
import random

import http.client

from django.conf import settings
from django.contrib.auth import authenticate, login

def send_otp(req):
    data = {'title': 'OTP'}
    # , email, otp, name
    if req.method == 'POST':
        email = { }
        # send_code(req)
    return render(req, 'two-factor.html', data)


# def send_code(request):
#     # send = forms.Send_Mail()
#     if request.method == 'POST':
#         EMAIL_HOST_USER = 'mediquick.adm1n@gmail.com'
#         # send = forms.Send_Mail(request.POST)
#         subject = 'Your Mediquick OTP'
#         message = 'Here is the OTP you requested from MediQuick'
#         # recipient --- from database
#         send_mail(subject, 
#             message, EMAIL_HOST_USER, [recipient], fail_silently = False)
#         return render(request, redirect('users-home'), {'recipient': recipient})
#     return render(request, 'two-factor.html')
