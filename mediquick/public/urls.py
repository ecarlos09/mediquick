from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('405-fobidden/', views.forbidden_405, name='405')
]