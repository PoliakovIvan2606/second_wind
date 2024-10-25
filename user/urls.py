from django.contrib.auth.views import LogoutView
from django.urls import path

from second_wind import settings
from . import views

app_name = 'user'

urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('login/', views.login_view, name='login'),
]
