from django.urls import path
from movie.views import kino_list, kino_detail


urlpatterns = [
    path('list/', kino_list, name='list'),
    path('detail/<int:id>/', kino_detail, name='detail')
]
