from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'chat/index.html', {})

# @login_required
def room(request, room_name):
    print("ROOM VIEW CONT")
    print(request.user.username)
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': request.user.username,
        'name': request.user.first_name,
        'last_name': request.user.last_name,
    })