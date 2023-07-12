from .models import Route
from django.forms import ModelForm

class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = ['lat1', 'long1', 'lat2', 'long2']