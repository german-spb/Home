from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import LoginForm, RegisterForm, CountersForm, DocumentForm, PayDataForm, BookForm
from django.views.generic.edit import FormView, CreateView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import datetime




@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def counters(request):
    return render(request, 'counters.html')

@login_required
def documents(request):
   owner = Document.objects.filter(owner='Дом')
   if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'documents.html', {'form': form, 'img_obj': img_obj, 'owner': owner})
   else:
        form = DocumentForm()
        return render(request, 'documents.html', {'form': form, 'owner': owner})

@login_required
def delete_document_home(request, file_id):
    file = Document.objects.get(id=file_id)
    return render(request, 'document_delete.html', {'file': file})

@login_required
def document_delete_home_confirm(request, file_id):
    Document.objects.get(id=file_id).delete()
    return redirect('/documents/')

@login_required
def document_view(request, file_id):
    file_record = Document.objects.get(id=file_id)
    return render(request, 'view.html', {'file_record' : file_record})

# ==================================Герман =============================================================================
@login_required
def documents_german_upload(request):
    owner = Document.objects.filter(owner='Герман')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'documents_german.html', {'form': form, 'img_obj': img_obj, 'owner': owner})
    else:
        form = DocumentForm()
    return render(request, 'documents_german.html', {'form': form, 'owner': owner})

@login_required
def document_delete_german_confirm(request, file_id):
    Document.objects.get(id=file_id).delete()
    return redirect('/documents_german/')
@login_required
def delete_document_german(request, file_id):
    file = Document.objects.get(id=file_id)
    return render(request, 'document_delete_german.html', {'file': file})

# ==================================Ирина===============================================================================
@login_required
def documents_irina_upload(request):
    owner = Document.objects.filter(owner='Ирина')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'documents_irina.html', {'form': form, 'img_obj': img_obj, 'owner': owner})
    else:
        form = DocumentForm()
    return render(request, 'documents_irina.html', {'form': form, 'owner': owner})

@login_required
def delete_document_irina(request, file_id):
    file = Document.objects.get(id=file_id)
    return render(request, 'document_delete_irina.html', {'file': file})
@login_required
def document_delete_irina_confirm(request, file_id):
    Document.objects.get(id=file_id).delete()
    return redirect('/documents_irina/')

# ===================================Марк===============================================================================
@login_required
def documents_mark_upload(request):
    owner = Document.objects.filter(owner='Марк')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'documents_mark.html', {'form': form, 'img_obj': img_obj, 'owner': owner})
    else:
        form = DocumentForm()
    return render(request, 'documents_mark.html', {'form': form, 'owner': owner})

@login_required
def delete_document_mark(request, file_id):
    file = Document.objects.get(id=file_id)
    return render(request, 'document_delete_mark.html', {'file': file})

@login_required
def document_delete_mark_confirm(request, file_id):
    Document.objects.get(id=file_id).delete()
    return redirect('/documents_mark/')


# ================================== Библиотека =======================================================================
@login_required
def book_upload(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'books.html', {'form': form, 'img_obj': img_obj, 'books': books})
    else:
        form = BookForm()
    return render(request, 'books.html', {'form': form, 'books': books})

@login_required
def delete_book(request, file_id):
    file = Book.objects.get(id=file_id)
    return render(request, 'book_delete.html', {'file': file})

@login_required
def delete_book_confirm(request, file_id):
    Book.objects.get(id=file_id).delete()
    return redirect('/book/')

@login_required
def download_book(request, filename):
    file_path = os.path.join(settings.STATIC_ROOT, 'files', filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = FileResponse(file)
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    else:
        return HttpResponse("File not found", status=404)




def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('home')

    # Render the login page template (GET request)
    return render(request, 'login.html')


def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)

        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # Set the user's password and save the user object
        user.set_password(password)
        user.save()

        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')

    # Render the registration page template (GET request)
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# def input_date(request):
#     form = CountersForm()
#     return render(request, 'input_date.html', {'form': form})

# ===========================Запись данных в БД из формы===============================================================
class SuccessView(TemplateView):
    template_name = 'success.html'

class CountersFormView(FormView):
    form_class = CountersForm
    template_name = 'input_date.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
# ------ получаем данные из формы ввода показаний счетчиков -------------------------------
     elec_day = self.request.POST.get('elec_day')
     elec_night = self.request.POST.get('elec_night')
     water = self.request.POST.get('water')
     gas = self.request.POST.get('gas')
# ----- если в БД нет ни одной записи, то "else" -------------------------------------------
     last_counter_elec_day = Counters.objects.order_by('elec_day').last()
     if last_counter_elec_day:
         last_counter_elec_night = Counters.objects.order_by('elec_night').last()
         last_counter_water = Counters.objects.order_by('water').last()
         last_counter_gas = Counters.objects.order_by('gas').last()
         outgo_elec_day = int(elec_day) - last_counter_elec_day.elec_day
         outgo_elec_night = int(elec_night) - last_counter_elec_night.elec_night
         outgo_water = int(water) - last_counter_water.water
         outgo_gas = int(gas) - last_counter_gas.gas
     else:
         outgo_elec_day = elec_day
         outgo_elec_night = elec_night
         outgo_water = water
         outgo_gas = gas
     form.save()
# ------------ берем последнюю запись в БД для определения ее id (objects.id) -------------------
     objects = Counters.objects.all().last()
     values_for_update = {'outgo_elec_day': outgo_elec_day, 'outgo_elec_night': outgo_elec_night, 'outgo_water': outgo_water, 'outgo_gas': outgo_gas}
     Counters.objects.update_or_create(id=objects.id, defaults=values_for_update)
     return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'В поле {field} возникла ошибка: {error}')
        return super().form_invalid(form)


# -------------- извлечение из БД --------------------------------------------------------------
def list_counters(request):
    counters = Counters.objects.order_by('year')
    data_pay = PayData.objects.all()
    form = PayDataForm()
    print(data_pay)
    return render(request, 'list_counters.html', {'counters': counters, 'form': form, 'data': data_pay})


@login_required
def all_delete (request):
    Counters.objects.all().delete()
    return HttpResponse('Все записи удалены')

# ------------ Удаление файлов------------------
@login_required
def delete_documents(request):
    Document.objects.all().delete()
    return HttpResponse('Все файлы удалены')


