from django.contrib import admin
from .models import Tour, Review, TourCategory

admin.site.register([Tour, Review, TourCategory])
