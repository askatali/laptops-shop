from django.contrib import admin
from shop.models import Laptop, Image


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = list_display

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'laptop', 'image')
    list_display_links = list_display
