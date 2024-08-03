from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=200)
    in_main_page = models.BooleanField(default=False)
    movie_category = models.CharField(max_length=100)