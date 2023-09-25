from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse

from .forms import LoginForm, UserRegistrationForm
from .models import Profile, User, SendHelp
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, DoctorRegistrationForm, \
    PatientMenuForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.views import LoginView
from django.core.signals import request_finished

# def index_account(request):
#     return render(request, 'main/index.html')


def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'account:dashboard'})


def register(request):
    print(request)
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            # new_user.save()
            # profile = Profile()
            # profile.user = new_user
            new_user.save()
            profile = Profile()
            profile.user = new_user
            profile.save()

            return render(request, 'account/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def register_doctor(request):
    if request.method == 'POST':
        user_form = DoctorRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            # new_user.save()
            # profile = Profile()
            # profile.user = new_user
            new_user.save()
            profile = Profile()
            profile.user = new_user
            profile.save()
            print(new_user.email)

            return render(request, 'account/doctor_register_done.html', {'new_user': new_user})

    else:
        user_form = DoctorRegistrationForm()
    return render(request, 'account/doctor_register.html', {'user_form': user_form})


@login_required
def function_menu_patient(request):
    profile_form = ProfileEditForm(instance=request.user.profile)
    user_form = UserEditForm(instance=request.user)
    if request.user.groups.filter(name='doctor').exists():
        return render(request, 'account/function_menu_doctor.html',
                      {'profile_form': profile_form, 'user_form': user_form})  # группы
    else:
        return render(request, 'account/function_menu_patient.html',
                      {'profile_form': profile_form, 'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'account/dashboard.html', {'section': 'account:dashboard'})  # если все окей
        return render(request, 'account/register.html')  # если НЕ все окей
    else:
        # if request.user.groups.filter(name='doctor').exists():
        #     return render(request, 'account/register.html')  # группы
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


def paitient_main_menu(request):
    if request.method == 'POST':
        patient_form = PatientMenuForm(data=request.POST)
        print(patient_form)
        # age = patient_form.cleaned_data['age']
        # problem = patient_form.cleaned_data['problem']
        # languages = patient_form.cleaned_data['languages']
        # full_name = patient_form.cleaned_data['full_name']
        # number = patient_form.cleaned_data['number']
        # address = patient_form.cleaned_data['address']
        # print(age, problem, languages, full_name, number, address)
        if patient_form.is_valid():
            patient_form.save()


    else:
        patient_form = PatientMenuForm()

    return render(request, 'account/paitient_main_menu.html', {'patient_form': patient_form})


def doctor_main_menu(request):
    if request.method == 'POST':
        return render(request, 'account/mapp.html')
    else:
        help = SendHelp.objects.all()
        return render(request, 'account/doctor_main_menu.html', {'help': help})
