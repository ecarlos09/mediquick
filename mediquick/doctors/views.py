from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from users.models import CustomUser

# Create your views here.

'''Error handling views'''
# def not_found_404(request, exception):
#     data = { 'err': exception }
#     return render(request, '404.html', data)

# def server_error_500(request):
#     return render(request, '500.html')

'''End of error handling views'''

@login_required
def doctor_home(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    pk = str(request.session.get('pk'))
    if user_id == pk and user.is_doctor:
        data = {
            'title': user_id,
            'user_number': user_id,
            'name': "Strange"
        }
        return render(request, 'doctors/doctor-home.html', data)
    else:
        return redirect('login')

''' Requires editing still '''
def doctor_schedule(request):
    name = "Strange"
    data = {
        "title": f'{name}\'s Schedule',
        "date": "17/05/2021"
    }
    return render(request, 'doctors/doctor-schedule.html', data)

def doctor_room(request):
    name = "Strange"
    data = {
        "title": f'{name}\'s Room',
    }
    return render(request, 'doctors/doctor-room.html', data)

''' End of doctor views '''

'''For reference'''

# def about(request):
#     return render(request, 'about.html')

# @login_required
# def books(request):
#     data = { 'booklist': Book.objects.all() }
#     return render(request, 'books.html', data)

# @login_required
# def create(request):
#     if request.method == 'POST':
#         book = NewBookForm(request.POST)
#         if book.is_valid():
#             book_id = book.save().id
#             return redirect("library-show", book_id=book_id)
#     else:
#         form = NewBookForm()
#     data = {'form': form }
#     return render(request, 'newbook.html', data)

# @login_required
# def show(request, book_id):
#         book = get_object_or_404(Book, pk=book_id)
#         if request.method == 'POST':
#             form = BorrowBookForm(request.POST)
#             if form.is_valid():
#                 book.borrower = request.user if not book.borrower else None
#                 book.save()
#                 return redirect("library-show", book_id=book_id)
#         else:
#             form = BorrowBookForm(initial={'borrower': request.user})
#         data = {
#             'book': book,
#             'form': form
#         }
#         return render(request, 'show.html', data)