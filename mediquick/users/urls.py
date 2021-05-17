from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.auth_view, name='login'),
    # path('register', views.index, name='index'),
    path('register', views.register, name='register'),
]