from django.urls import path
from .views import LaptopView, LaptopCreateAPIView

urlpatterns = [
    path('laptop/', LaptopView.as_view(), name='laptop'),
    path('create/', LaptopCreateAPIView.as_view(), name='create'),




]