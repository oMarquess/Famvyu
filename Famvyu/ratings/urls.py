from django.contrib import admin
from django.urls import path
from .views import ratings

urlpatterns = [
    path('', ratings.as_view(), name='movies'),
]