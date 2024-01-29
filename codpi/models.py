from django.db import models


class Laptop(models.Model):

    BRAND_CHOICES =[
        ('lenovo', 'LENOVO'),
        ('hp', 'HP'),
        ('dell', 'DELL'),
        ('acer', 'ACER'),
        ('asus', 'ASUS'),
        ('samsung', 'SAMSUNG'),
    ]

    MEMORI_CHOICES =[
        ('256', '256'),
        ('512', '512'),
        ('1', '1'),
    ]

    CURRENCY_CHOICES =[
        ('usa', 'USA'),
        ('сом', 'СОМ'),
        ('юань', 'ЮАНЬ'),
    ]

    brand = models.CharField(max_length=80)
    title = models.CharField(max_length=80)
    memory = models.IntegerField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(upload_to='image/laptop/')
    currency = models.CharField(default='USA', max_length=30)


class Phone(models.Model):

    PHONE_CHOICES = [
        ('samsung', 'Samsung'),
        ('apple', 'Apple'),
        ('huawei', 'Huawei'),
        ('google', 'Google'),
        ('xiaomi', 'Xiaomi'),
    ]

    MEMORY_CHOICES = [
        ('128', '128'),
        ('256', '256'),
        ('256', '256'),
    ]

    brand = models.CharField(max_length=80, choices=PHONE_CHOICES)
    memory = models.IntegerField()
    price = models.FloatField()
    color = models.CharField(max_length=30, default='Black')
    image = models.ImageField(upload_to='image/phone/')
    description = models.TextField(blank=True, null=True)


class Shop(models.Model):
    COLORS_CHOICES = [
        ('pink', 'Розовый'),
        ('black', 'Черный'),
        ('blue', 'Синий'),
    ]

    SIZE_CHOICES = [
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
        ('xxxl', 'XXXL')
    ]

    STYLE_CHOICES = [
        ('casual', 'Повседневный'),
        ('sports', 'Спортивный'),
    ]

    BRAND_CHOICES = [
        ('nike', 'Nike'),
        ('adidas', 'Adidas'),
        ('puma', 'Puma'),
        ('reebok', 'Reebok'),
        ('asics', 'Asics'),
    ]
    PRICE_CHOICE = [
        (1, 1000),
        (2, 2000),
    ]

    brand = models.CharField(max_length=80, choices=BRAND_CHOICES, default='nike')
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, default='xl')
    color = models.CharField(max_length=15, choices=COLORS_CHOICES, default='pink')
    style = models.CharField(max_length=25, choices=STYLE_CHOICES, default='sports')
    image = models.ImageField(upload_to='image/cloth/')
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(choices=PRICE_CHOICE, default=1)
    sportswear_description = models.TextField(blank=True, null=True, verbose_name='Описание спортивной одежды')


class Wallet(models.Model):
    title = models.CharField(max_length=80)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE,
                                 related_name='wallet')


class Customer(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.name}'


















