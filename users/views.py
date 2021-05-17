from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm

# Create your views here.
def register(req):
    if req.method == 'POST':
        form = UserSignupForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Welcome {username}!') # change to the login page
            return redirect('user-home') #change to the login page
    else:
        form = UserSignupForm()
        data = { 'form': form }
        return render(req, 'register.html', data)