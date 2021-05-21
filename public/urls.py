from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forbidden/', views.forbidden_405, name='405'),
    path('not-found/', views.not_found_404, name='404'),
    path('server-error/', views.server_error_500, name='500'),
    path('policy/', views.policy, name='policy'),
    path('support/', views.support, name='support'),
    path('testimonials/', views.testimonials, name='testimonials'),
]