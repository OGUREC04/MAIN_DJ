from django.db import models
from django.conf import settings


class NumberDemo(models.Model):
    number = models.IntegerField()
    number_name = models.CharField(max_length=64)
