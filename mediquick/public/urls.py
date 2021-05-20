from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.not_found_404, name='404'),
    path('', views.forbidden_405, name='405'),
    path('', views.server_error_500, name='500'),
    path('policy/', views.policy, name='policy'),
    path('about/', views.about, name='about'),
    path('support/', views.support, name='support'),
]