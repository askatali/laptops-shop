from django.contrib import admin
from codpi.models import Laptop, Phone


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('brand',)


admin.site.register(Phone, PhoneAdmin)
