from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('welcome/', views.login, name='login')
]