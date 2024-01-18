from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 255)
    image_url = models.URLField(default ='')
    year = models.CharField(max_length = 4) #assumes year is always in YYYY format
    duration = models.CharField(max_length = 10) #ex.: '3h 1m'
    star_rating = models.DecimalField(max_digits = 3, decimal_places = 1) #ex.: '8.0'
    rate_count = models.CharField(max_length = 100, blank = True, null = True) #rate count can be option
    product_url = models.URLField(default = '')