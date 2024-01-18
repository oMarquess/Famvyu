from django.shortcuts import render
from .models import Movie
from django.views.generic import ListView

# Create your views here.

class movies(ListView):
    model = Movie
    template_name = "movies.html"
    context_object_name = "movie"
    fields = ["title"]
