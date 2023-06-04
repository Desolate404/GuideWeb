from rest_framework import serializers
from .models import Souvenir, SouvenirCategory


class SouvenirCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SouvenirCategory
        fields = '__all__'


class SouvenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souvenir
        fields = '__all__'
