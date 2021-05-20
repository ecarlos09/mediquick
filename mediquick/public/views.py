from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'public/home.html')

def not_found_404(request, exception):
    return render(request, '404.html')

def forbidden_405(request):
    return render(request, '405.html')   

def server_error_500(request):
    return render(request, '500.html')    


# def login(request):
#     return render(request, 'public/login.html', title="login")

# render testimonials

#render footer

def policy(request):
    return render(request, 'public/policy.html')

def about(request):
    return render(request, 'public/about.html')

def support(request):
    return render(request, 'public/support.html')
