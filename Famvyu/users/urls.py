from django.contrib import admin
from django.urls import path
from .views import index, about, services

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name = 'about'),
    path('services/', services, name = 'services')
]
