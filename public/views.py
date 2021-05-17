from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'public/home.html')

    
def login(request):
    
    return render(request, 'public/login.html', title="login")