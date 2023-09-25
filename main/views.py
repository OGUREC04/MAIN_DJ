from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UserForm, EmailForm
from .send_email import send_email


def main_page(request):
    if request.method == 'POST':
        email = EmailForm(request.POST)
        if email.is_valid():
            em = email.cleaned_data.get("em")
            send_email(em)

        form = UserForm(request.POST)
        if form.is_valid():
            print(form)
            new_number = form.save(commit=False)
            new_number.save()
            # number_name = form.cleaned_data.get("number_name")
            # number = form.cleaned_data.get("number")
            # print(number, number_name)
    # num_authors = Author.objects.count()  # The 'all()' is implied by default.
    #
    # # Number of visits to this view, as counted in the session variable.
    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1

    return render(request, 'main/main_page.html')


def index(request):
    data = {
        'title': 'Главная страница',
        'text': 'Тут будет какой то классный и полезый текст...'
    }
    return render(request, 'main/index.html', data)


def map(request):
    return render(request, 'main/ph.html')


def doc_register(request):
    return render(request, 'main/doc_register.html')


def doctor_main_menu(request):
    return render(request, 'main/Doctor_main_menu.html')


def paitient_main_menu(request):
    return render(request, 'main/paitient_main_menu.html')


def team(request):
    return render(request, 'main/team.html')

def faq(request):
    return render(request, 'main/faq.html')
