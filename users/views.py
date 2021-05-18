from django.contrib.auth.models import AnonymousUser
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm

#two factor auth

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from codes.forms import CodeForm
from .models import CustomUser

#two factor end

# Create your views here.
def register(req):
    form = UserSignupForm()
    print(form)
    print(req.method == 'POST')
    if req.method == 'POST':
        form = UserSignupForm(req.POST)
        # form = UserSignupForm(data=req.POST)
        print(f'is form valid? {form.is_valid()}')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Welcome {username}!') # change to the login page
            # return redirect('user-home') #change to the login page
            # return render(req, 'registered')
            # request.session['pk'] =user.pk
            return redirect('two-factor-code')
        else: 
            return render(req, 'register.html', {'form': form})
    else:
        # form = UserSignupForm()
        # data = { 'form': form }
        return render(req, 'register.html', {'form': form})

        # handle login 

# from the example main view
#two factor auth

# login

def auth_view(request):
    form = AuthenticationForm(request.POST)
    # if form.is_valid():
    # print(form.is_valid)
    if request.method == "POST":
        print(request.POST)
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        user = authenticate(username=username_input, password=password_input)
        print(user)
        if user is not None:
            # request.session['pk']=user.pk
            # form = CodeForm(request.POST or None)
            # return render(request, 'verify.html')
            return redirect('/verify')
    return render(request, 'login.html', {'form': form})

    
# @login_required
def verify_view(request):
    # print("user is")
    # print(request.user)
    # if request.user is not AnonymousUser:
    # csrf = request['cs']
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')

    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        code_user = f"{user.username}: {user.code}"
        if not request.POST:
            print(code_user)
            # send email

        print(f'is form valid? : {form.is_valid()}')
        #does form.valid does not work
        if form.is_valid():
            num = form.cleaned_data.get('number')
            print(num)
            if str(code) == num:
                code.save()
                login(request, user)
                return authenticated(request)
            else:
                print("redirecting to login")
                return redirect('/login')
    return render(request, 'verify.html', {'form': form})




def authenticated(request):
    return HttpResponse("hello")

#two factor end









                

