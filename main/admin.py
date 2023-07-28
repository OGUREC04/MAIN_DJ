from django.contrib import admin

# Register your models her
from articles.models import Article, Comment
from main.models import NumberDemo
from account.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


admin.site.register(NumberDemo)
admin.site.register(Profile, ProfileAdmin)
