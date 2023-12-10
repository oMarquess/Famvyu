from django.shortcuts import render, redirect, get_object_or_404
from movies.models import Movie, Suggestion
from ratings.models import MovieRating
from django.db.models import Avg, Count, Max
from .forms import SuggestionForm
from django.contrib import messages
from collections import Counter

import random
import wikipediaapi
#from movies.utils import get_movie_description

def index(request):
    all_movies = list(Movie.objects.all())
    random_movies = random.sample(all_movies, min(len(all_movies), 6))

    movies_with_ratings = []
    for movie in random_movies:
        ratings = MovieRating.objects.filter(movie=movie)

        if ratings.exists():
            average_rating = ratings.aggregate(Avg('overall_rating'))['overall_rating__avg']
            # Additional aggregated data
            mood_types = list(ratings.values_list('mood_type', flat=True).distinct())
            age_recommendations = list(ratings.values_list('age_recommendation', flat=True).distinct())
            theme_labels = list(ratings.values_list('theme_label', flat=True).distinct())
        else:
            average_rating = 'No ratings yet'
            mood_types, age_recommendations, theme_labels = [], [], []

        movies_with_ratings.append({
            'movie': movie,
            'title': movie.title,
            'year': movie.year,
            'duration': movie.duration,
            'star_rating': movie.star_rating,
            'average_rating': average_rating,
            #'mood_types': mood_types,
            #'age_recommendations': age_recommendations,
            #'theme_labels': theme_labels,
            'image_url': movie.image_url if movie.image_url else None
        })

    return render(request, 'index.html', {'movies_with_ratings': movies_with_ratings})

