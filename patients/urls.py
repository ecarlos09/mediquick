from django.urls import path, include
from . import views


urlpatterns = [
    path('home/logout', views.logout, name='logout'),
    path('home/<user_id>', views.patient_home, name='patient-home'),
    path('', include('django.contrib.auth.urls')),

]