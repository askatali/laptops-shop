from rest_framework import serializers
from shop.models import Laptop, Image


class LaptopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ('id', 'price', 'image')


class CreateLaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ('name', 'price', 'image', 'description', 'color','state')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')

