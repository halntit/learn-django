from django.contrib import admin

# Register your models here.
from .models import Product #.models: dot is the same folder --> .models --> file models

admin.site.register(Product)