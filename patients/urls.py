from django.urls import path
from . import views

urlpatterns = [
    path('home/<user_id>', views.patient_home, name='patient-home'),
]