from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.send_otp, name='user-otp')
]