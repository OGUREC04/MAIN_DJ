from main.models import NumberDemo
from django import forms


class UserForm(forms.ModelForm):
    # number_name = forms.CharField(max_length=100)
    # number = forms.IntegerField()
    class Meta:
        model = NumberDemo
        fields = ["number", "number_name"]


class EmailForm(forms.Form):
    em = forms.EmailField()

