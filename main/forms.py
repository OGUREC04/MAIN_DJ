from main.models import NumberDemo
from django import forms


class UserForm(forms.ModelForm):
    # number_name = forms.CharField(max_length=100)
    # number = forms.IntegerField()
    email = forms.EmailField()

    class Meta:
        model = NumberDemo
        fields = ["number_name", "company", "email", "number"]


class EmailForm(forms.Form):
    em = forms.EmailField()
