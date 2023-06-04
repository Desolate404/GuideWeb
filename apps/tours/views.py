from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from ..favorites.serializers import FavoriteSerializer
from .models import Tour, TourCategory
from .serializers import ReviewSerializer, TourSerializer, TourCategorySerializer


class TourCategoryViewSet(viewsets.ModelViewSet):
    queryset = TourCategory.objects.all()
    serializer_class = TourCategorySerializer

    def get_permissions(self):
        if self.request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            return (permissions.IsAdminUser(),)
        return (permissions.AllowAny(),)


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()

    def get_permissions(self):
        if self.action in ('review', 'favorite'):
            return [permissions.IsAuthenticated()]
        elif self.request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def get_serializer_class(self):
        if self.action == 'review':
            return ReviewSerializer
        elif self.action == 'favorite':
            return FavoriteSerializer
        return TourSerializer

    @action(['POST'], detail=True)
    def review(self, request, pk=None):
        tour = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(tour=tour, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(['POST'], detail=True)
    def favorite(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
