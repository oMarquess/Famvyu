from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ratings(request):
    return render(request, "ratings.html")