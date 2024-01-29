from django.shortcuts import render
from movie.models import Movie


def kino_render(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'kino.html', context={'movie': movie})


def kino_list(request):
    movies = Movie.objects.all()
    return render(request, 'list.html', context={'movies': movies})

