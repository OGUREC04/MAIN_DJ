from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('index', views.index, name='index'),
    path('map', views.map, name='map'),
    path('doc_register', views.doc_register, name='doc_register'),
    path('doctor_main_menu', views.doctor_main_menu, name='doctor_main_menu'),
    path('paitient_main_menu', views.paitient_main_menu, name='paitient_main_menu'),

]
