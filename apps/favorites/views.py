from rest_framework.generics import ListAPIView

from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteList(ListAPIView):
    serializer_class = FavoriteSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(user=user)
