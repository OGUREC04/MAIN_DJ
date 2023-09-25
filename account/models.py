from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.first_name)


class SendHelp(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    CHOICES = [
        ('1', 'NOT_Child'),
        ('2', 'Child'),
    ]
    age = models.CharField(
        max_length=10,
        choices=CHOICES,
    )
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    problem = models.CharField(max_length=1000)
    type_danger = models.CharField(max_length=1000)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    number = models.IntegerField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




