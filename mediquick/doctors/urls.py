
from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_home, name='doctor-home'),
    path('schedule/', views.doctor_schedule, name='doctor-schedule'),
    path('room/', views.doctor_room, name='doctor-room'),
    # path('about/', views.about, name='library-about'),
    # path('books/', views.books, name='library-books'),
    # path('books/new/', views.create, name='books-create'),
    # path('books/<int:book_id>', views.show, name='library-show'),
]