from django.db import models


class Laptop(models.Model):
    title = models.CharField(max_length=80)
    memory = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='laptop/')
    currency = models.CharField(default='USA', max_length=30)


class Phone(models.Model):
    brand = models.CharField(max_length=80)
    memory = models.IntegerField()
    price = models.FloatField()
    color = models.CharField(max_length=30, default='Black')
    image = models.ImageField(upload_to='phone/')
    description = models.TextField(blank=True, null=True)
