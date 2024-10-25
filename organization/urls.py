from django.urls import path
from . import views

app_name = 'organization'

urlpatterns = [
    path('index/', views.index, name='home'),
    path('index2/', views.index2, name='index2'),
]
