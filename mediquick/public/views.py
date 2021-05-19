from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'public/home.html')

def forbidden_405(request):
    return render(request, 'public/errors/405.html')

    
# def login(request):
#     return render(request, 'public/login.html', title="login")

# render testimonials

#render footer