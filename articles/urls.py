from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index_second, name='index_second'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment', views.leave_comment, name='leave_comment')
]
