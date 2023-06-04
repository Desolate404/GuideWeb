from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from ..favorites.serializers import FavoriteSerializer
from .models import Food, FoodCategory
from .serializers import FoodSerializer, FoodCategorySerializer


class FoodCategoryViewSet(ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

    def get_permissions(self):
        if self.request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            return (IsAdminUser(),)
        return (AllowAny(),)


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()

    def get_permissions(self):
        if self.action in ('favorite',):
            return (IsAuthenticated(),)
        elif self.request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            return (IsAdminUser(),)
        return (AllowAny(),)

    def get_serializer_class(self):
        if self.action in ('favorite',):
            return FavoriteSerializer
        return FoodSerializer

    @action(['POST'], detail=True)
    def favorite(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
