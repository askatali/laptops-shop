from django.urls import path
from .views import LaptopListView, LaptopCreateAPIView, LaptopDetailView, LaptopUpdateAPIView, LaptopDeleteAPIView

urlpatterns = [
    path('laptop/', LaptopListView.as_view(), name='laptop'),
    path('create/', LaptopCreateAPIView.as_view(), name='create'),
    path('detail/<int:id>/', LaptopDetailView.as_view(), name='detail'),
    path('update/<int:id>', LaptopUpdateAPIView.as_view(), name='update'),
    path('delete/<int:id>', LaptopDeleteAPIView.as_view(), name='delete'),



]