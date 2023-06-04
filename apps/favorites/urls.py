from django.urls import path

from .views import FavoriteList

urlpatterns = [
    path('favorites', FavoriteList.as_view()),
]
