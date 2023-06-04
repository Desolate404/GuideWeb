from django.contrib import admin
from .models import Forum, Topic, Comment

admin.site.register([Forum, Topic, Comment])