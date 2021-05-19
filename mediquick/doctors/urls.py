
from django.urls import path
from . import views

urlpatterns = [
    path('home/<user_id>', views.doctor_home, name='doctor-home'),
    path('schedule/', views.doctor_schedule, name='doctor-schedule'),
    path('room/', views.doctor_room, name='doctor-room'),
]