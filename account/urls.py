from django.contrib.auth.views import logout_then_login, LoginView, LogoutView, PasswordChangeView, \
    PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, reverse_lazy

from . import views

app_name = 'account'
urlpatterns = [
    # post views
    # path('', views.index_account, name='index_account'),
    # path('', views.user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('', views.dashboard, name='dashboard'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(),  name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('doctor_register/', views.register_doctor, name='doctor_register'),
    path(r'edit/', views.edit, name='edit'),
    path(r'function_menu_patient/', views.function_menu_patient, name='function_menu_patient'),
    path(r'paitient_main_menu/', views.paitient_main_menu, name='paitient_main_menu'),
    # path('user/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    # path('user/<str:slug>/', ProfileDetailView.as_view(), name='profile_detail'),

]
