from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
# from guardian.decorators import permission_required_or_403

# Create your views here.

# def not_found_404(request, exception):
#     data = { 'err': exception }
#     return render(request, '404.html', data)

# def server_error_500(request):
#     return render(request, '500.html')

# @permission_required_or_403('auth.change_group',
# (Group, 'name', 'group_name'))
def doctor_home(request):
    title = "Your Profile"
    name = "Strange"
    data = {
        "title": title,
        "name": name
    }
    return render(request, 'doctor-home.html', data)

def doctor_schedule(request):
    name = "Strange"
    data = {
        "title": f'{name}\'s Schedule',
        "date": "17/05/2021"
    }
    return render(request, 'doctor-schedule.html', data)

def doctor_room(request):
    name = "Strange"
    data = {
        "title": f'{name}\'s Room',
    }
    return render(request, 'doctor-room.html', data)

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