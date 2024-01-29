from django.contrib import admin
from codpi.models import Laptop, Phone,Shop, Customer, Wallet


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('brand',)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand',)


admin.site.register(Customer)
admin.site.register(Wallet)

