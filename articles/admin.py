from django.contrib import admin

# Register your models her
from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)