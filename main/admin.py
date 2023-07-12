from django.contrib import admin

# Register your models her
from articles.models import Article, Comment
from main.models import NumberDemo


admin.site.register(NumberDemo)
