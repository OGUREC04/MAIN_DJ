from django.db import models

# Create your models here.
from django.db.models import FloatField


class Route(models.Model):
    lat1 = FloatField('ширина1')
    long1 = FloatField('долгота1')
    lat2 = FloatField('ширина2')
    long2 = FloatField('долгота2')

