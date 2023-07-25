from django.urls import path
from . import views
from .views import *

from django.contrib.auth import views as auth_views
from .forms import ResetPasswordForm,NewPasswordForm

from django.contrib import admin




urlpatterns = [
    path('signupClient', ClientSignUpView.as_view(), name='signupClient'),
    path('signupAdmin', AdminSignUpView.as_view(), name='signupAdmin'),
    path('login', views.Login, name='login'),
    path('logout', views.logout_user, name= 'logout' ),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="registration/reset_password.html"), name="password_reset"),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/reset_password_done.html"), name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/reset_password_confirm.html"), name="password_reset_confirm"),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/reset_password_complete.html"), name="password_reset_complete"),

]

'''
    path('reset_password/', views.auth.PasswordResetView.as_view(template_name="registration/reset-password.html", form_class= ResetPasswordForm), name= 'reset_password' ),

    path('reset_password_sent/done/', views.PasswordResetDoneView.as_view(template_name="registration/reset_password_done.html"), name= 'reset_password_done' ),

    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="registration/reset_password_confirm.html", form_class= NewPasswordForm), name= 'password_reset_confirm' ),
    
    path('reset_password_complete/', views.PasswordResetCompleteView.as_view(template_name="registration/reset_password_complete.html"), name= 'reset_password_complete' ),
'''