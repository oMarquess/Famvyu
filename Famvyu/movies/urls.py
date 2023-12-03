from django.contrib import admin
from django.urls import path
from .views import movies

urlpatterns = [
    path('', movies, name='movies'),
]