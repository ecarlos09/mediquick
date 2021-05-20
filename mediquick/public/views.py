from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'public/home.html')

def forbidden_405(request):
    return render(request, 'public/errors/405.html')

def not_found_404(request):
    return render(request, 'public/errors/404.html')

def server_error_500(request):
    return render(request, 'public/errors/500.html')
    
# def login(request):
#     return render(request, 'public/login.html', title="login")

# render testimonials
def policy(request):
    return render(request, 'public/policy.html')

def support(request):
    return render(request, 'public/support.html')

def testimonials(request):
    return render(request, 'public/testimonials.html')

#render footer