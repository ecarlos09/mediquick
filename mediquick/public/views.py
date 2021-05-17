from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'public/home.html')

    
# def login(request):
#     return render(request, 'public/login.html', title="login")
