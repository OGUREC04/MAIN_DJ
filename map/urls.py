from django.urls import path

from . import views

app_name = 'map'
urlpatterns = [
    # post views
    # path('', views.index_account, name='index_account'),
    # path('', views.user_login, name='login'),
    path('<str:lat1>,<str:long1>,<str:lat2>,<str:long2>', views.showroute, name='showroute'),
    path('', views.showmap, name='showmap'),

]
