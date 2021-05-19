from django.contrib.auth.models import AnonymousUser
from django.core.mail import send_mail
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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
            password = form.cleaned_data.get('password1')
            messages.success(req, f'Welcome {username}!') # change to the login page
            # return redirect('user-home') #change to the login page
            # return render(req, 'registered')
            # request.session['pk'] =user.pk
            # return redirect('two-factor-code')
            user = authenticate(username=username, password=password)
            user_id = req.session['pk']=user.pk
            return redirect(f'/verify/{user_id}')
        else: 
            return render(req, 'register.html', {'form': form})
    else:
        # form = UserSignupForm()
        # data = { 'form': form }
        return render(req, 'register.html', {'form': form})


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
            user_id = request.session['pk']=user.pk
            # form = CodeForm(request.POST or None)
            # return render(request, 'verify.html')
            # return redirect('/verify/')
            return redirect(f'/verify/{user_id}')
    return render(request, 'login.html', {'form': form})

    
# @login_required
# def verify_view(request):
#     # print("user is")
#     # print(request.user)
#     # if request.user is not AnonymousUser:
#     # csrf = request['cs']
#     form = CodeForm(request.POST or None)
#     # form.save()
#     for key, value in request.session.items():
#         print('{} => {}'.format(key, value))
#     pk = request.session.get('pk')
    
#     print(pk)
#     if pk:
#         user = CustomUser.objects.get(pk=pk)
#         code = user.code
#         code_user = f"{user.username}: {user.code}"
#         if not request.POST:
#             print(code_user)
#             # send email

#         print(f'is form valid? : {form.is_valid()}')
#         #does form.valid does not work
#         if form.is_valid():
#             num = form.cleaned_data.get('number')
#             print(num)
#             if str(code) == num:
#                 code.save()
#                 login(request, user)
#                 return authenticated(request)
#             else:
#                 print("redirecting to login")
#                 return redirect('/login')
#     return render(request, 'verify.html', {'form': form})

def verify_view(request, user_id):    
#     print(pk)
#     if pk:
    if user_id:
            # print(request.user)
            # if request.user is not AnonymousUser:
        # csrf = request['cs']
        user = get_object_or_404(CustomUser, pk=user_id)
        form = CodeForm(request.POST or None)
        # pk = request.session.get('pk')
        
            #return redirect('/login')
        # print("key value pairs")
        # for key, value in request.session.items():
        #     print('{} => {}'.format(key, value))
        # pk = request.session.get('pk')    
        # user = CustomUser.objects.get(pk=pk)
        user = CustomUser.objects.get(pk=user_id)
        code = user.code
        code_user = f"{user.username}: {user.code}"

        if not request.POST:

            print(code_user)
#             # send email
            print(form)
            print(user)
            print('sending email')
            # EMAIL_HOST_USER = 'mediquick.adm1n@outlook.com'
            # subject = 'OTP with MediQuick'
            # code = user.code #54321 # change to generated code
            # message = f'Here is your OTP: {code}.'
            # recipient = user.email #'elwin.carlos09@gmail.com' # change to user
            # print(f'EMAIL RECIPIENT: {recipient}')

            # send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently = False)
            print('email sent')
            print(f'is form valid? : {form.is_valid()}')
            #does form.valid does not work
            # form.save()

            # if form.is_valid():
            print(f'verification form: {form}')
            # num = form.cleaned_data.get('number')
            # print(request.POST)
            # num = form['name']
            # print(num)
            # print(code_user)
        else:   
            if form.is_valid():
                num = form.cleaned_data.get("number")
                print(f'number is {num}')
                if str(code) == num:
                    code.save()
                    login(request, user)
                    # user_name = user.first_name
                    if user.is_doctor:
                        return redirect(f'/doctors/home/{user_id}')
                    else:
                        return redirect(f'/patients/home/{user_id}')
            else:
                print("redirecting to login")

        return render(request, 'verify.html', {'form': form})

#two factor end       