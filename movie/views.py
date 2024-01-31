from django.shortcuts import render
from movie.models import Movie


def kino_list(request):
    movies = Movie.objects.all()
    return render(request, 'list.html', context={'movies': movies})


def kino_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'detail.html', context={'movie': movie})
