from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'public/home.html')

@login_required
def user_home(request):
    return render(request, 'public/user-home.html') 