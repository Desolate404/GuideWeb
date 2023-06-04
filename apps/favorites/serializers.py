from rest_framework import serializers

from .models import Favorite
from ..clothes.serializers import ClothingSerializer
from ..food.serializers import FoodSerializer
from ..souvenirs.serializers import SouvenirSerializer
from ..tours.serializers import TourSerializer


class FavoriteListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        repr_ = [{
            'tour': TourSerializer(
                instance.tour).data if instance.tour else None,
            'food': FoodSerializer(
                instance.food).data if instance.food else None,
            'souvenir': SouvenirSerializer(
                instance.souvenir).data if instance.souvenir else None,
            'clothing': ClothingSerializer(
                instance.clothing).data if instance.clothing else None,
        }for instance in data]
        return repr_


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        read_only_fields = ('tour', 'souvenir', 'food', 'clothing', 'user')
        list_serializer_class = FavoriteListSerializer

    def validate(self, attrs):
        user = self.context['request'].user
        object = self.context['view'].get_object()
        object_name = object._meta.model_name
        object_dir = {object_name: object}

        if Favorite.objects.filter(user=user, **object_dir).exists():
            Favorite.objects.filter(user=user, **object_dir).delete()
            attrs['liked'] = False
        else:
            Favorite.objects.create(user=user, **object_dir)
            attrs['liked'] = True
        return attrs

    def to_representation(self, instance):
        return instance
