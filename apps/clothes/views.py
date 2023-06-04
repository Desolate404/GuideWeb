from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from ..favorites.serializers import FavoriteSerializer
from .models import ClothingCategory, Clothing
from .serializers import ClothingCategorySerializer, ClothingSerializer


class ClothingCategoryViewSet(ModelViewSet):
    queryset = ClothingCategory.objects.all()
    serializer_class = ClothingCategorySerializer

    def get_permissions(self):
        if self.request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            return (IsAdminUser(),)
        return (AllowAny(),)


class ClothingViewSet(ModelViewSet):
    queryset = Clothing.objects.all()

    def get_permissions(self):
        if self.action in ('favorite',):
            return (IsAuthenticated(),)
        elif self.request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            return (IsAdminUser(),)
        return (AllowAny(),)

    def get_serializer_class(self):
        if self.action in ('favorite',):
            return FavoriteSerializer
        return ClothingSerializer

    @action(['POST'], detail=True)
    def favorite(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
