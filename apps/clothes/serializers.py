from rest_framework import serializers
from .models import Clothing, ClothingCategory


class ClothingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingCategory
        fields = '__all__'


class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = '__all__'
