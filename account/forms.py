from django import forms
from django.contrib.auth.models import User
from .models import Profile

from django.contrib.auth.models import AbstractUser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    # username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # surname = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            self.add_error("password2", "asdasdasdasd")
            # raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class DoctorRegistrationForm(forms.ModelForm):
    # username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # surname = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = ('first_name', 'username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            self.add_error("password2", "asdasdasdasd")
            # raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "input"}))

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email')


class ProfileEditForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={"id": "imageUpload"}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"class": "date_edit", "type": "date"}))

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


class PatientMenuForm(forms.Form):
    CHOICES = [
        ('1', ''),
        ('2', ''),
    ]
    age = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={"type": "radio", "name": "radio", "class": "delete"}),
        choices=CHOICES,
    )
    problem = forms.CharField(widget=forms.Textarea(attrs={"id": "comment_text", "placeholder": "256 символов", "class": "ui-autocomplete-input", "cols": "40" }))
    languages = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={"id": "multi-select", "name": "states", "class": "ui selection dropdown"}), choices=((1, "Болит голова"), (2, "Болит горло"), (3, "Что то еще болит")))
    full_name = forms.CharField(widget=forms.TextInput(attrs={"id": "fullname", "class": "input", "placeholder":"Введите ФИО в свободной форме"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"id": "address", "class": "input", "placeholder": "Введите адрес в свободной форме"}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "input", "type": "tel",  "placeholder": "Номер (8 999 999 99 99)"}))

