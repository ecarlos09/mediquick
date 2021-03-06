from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from users.models import CustomUser

# Create your views here.

# def not_found_404(request, exception):
#     data = { 'err': exception }
#     return render(request, '404.html', data)

# def server_error_500(request):
#     return render(request, '500.html')

@login_required
def patient_home(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    pk = str(request.session.get('pk'))
    # print(f'pk: {type(pk)}')
    # print(f'user id: {type(user_id)}')
    # print(f'{pk==user_id}')
    # user_name = user.first_name
    if user_id == pk and not user.is_doctor:
        data = {
            'title': user_id,
            'user_number': user_id,
        }
        return render(request, 'patients/patient-home.html', data)
    else:
        return redirect('login')

# def schedule_appointment(request):
#     data = {

#     }
#     return render(request, 'schedule-appointment.html', data)