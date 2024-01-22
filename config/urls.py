
from django.contrib import admin
from django.urls import path
from codpi.views import index, my_url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('my_url/', my_url)
]

