from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    print(request.user.username)

    if request.user.first_name == "":
        name = "Admin"
    else: 
        name = request.user.first_name
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': request.user.username,
        'name': name,
        'last_name': request.user.last_name,
    })