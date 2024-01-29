from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=80)
    genre = models.CharField(max_length=80)
    year = models.CharField(max_length=20)
    country = models.CharField(max_length=70)
    description = models.TextField()
    director = models.CharField(max_length=80)
    image = models.ImageField(upload_to='image/movie/')
    star = models.FloatField(default=0.0)
    youtube_url = models.URLField(blank=True, null=True)
