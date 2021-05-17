from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from .models import Profile
import random

import http.client

from django.conf import settings
from django.contrib.auth import authenticate, login

def send_otp(req):
    data = {'title': 'OTP'}
    return render(req, 'two-factor.html', data)
    # if req.method == 'POST':


