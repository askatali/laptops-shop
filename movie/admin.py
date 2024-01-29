from django.contrib import admin
from movie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display

