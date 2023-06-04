from django.contrib import admin
from .models import Clothing, ClothingCategory

admin.site.register([Clothing, ClothingCategory])
