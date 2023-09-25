from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class NumberDemo(models.Model):
    number = models.IntegerField()
    number_name = models.CharField(max_length=64)
    company = models.CharField(max_length=128)
    email = models.CharField(max_length=128)


