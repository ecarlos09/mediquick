from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.auth_view, name='login'),
    path('register/', views.register, name='register'),
    path('verify/', views.verify_view, name='two-factor-code'),
]