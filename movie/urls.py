from django.urls import path
from movie.views import kino_render, kino_list


urlpatterns = [
    path('detail/<int:pk>/', kino_render, name='html'),
    path('list/', kino_list, name='list')
]

