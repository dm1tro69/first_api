from django.contrib import admin
from .models import Manufacturer, Product

# Register your models here.
admin.site.register(Product)

admin.site.register(Manufacturer)

