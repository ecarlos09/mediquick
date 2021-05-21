from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    return render(request, 'chat/index.html', {})


@login_required(login_url='/login/')
def room(request, room_name):
    print(request.user.username)

    if request.user.first_name == "":
        name = "Admin"
    else: 
        name = request.user.first_name
    return render(request, 'chat/room.html', {
        'user_number': request.user.id,
        'room_name': room_name,
        'username': request.user.username,
        'name': name,
        'last_name': request.user.last_name,
    })

@login_required
def logout(request):
    logout(request)
    return render(request, 'patients/logout.html')
