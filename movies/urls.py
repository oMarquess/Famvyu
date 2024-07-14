from django.contrib import admin
from django.urls import path
from .views import movies

urlpatterns = [
    path('', movies.as_view(), name='movies'),
]