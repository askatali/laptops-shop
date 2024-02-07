from django.db import models


class Laptop(models.Model):
    name = models.CharField(max_length=80)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='laptop/')
    description = models.TextField()
    color = models.CharField(max_length=40)
    state = models.CharField(max_length=50)

    class Meta:
        db_table = 'laptop'

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='laptops')
    image = models.ImageField(upload_to='image/')

    class Meta:
        db_table = 'image'

    def __str__(self):
        return f'{self.laptop.name}'
