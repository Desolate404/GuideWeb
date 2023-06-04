from rest_framework import serializers

from .models import Tour, Review, TourCategory


class TourCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourCategory
        fields = '__all__'


class TourListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        return [{
            ''
        }
            for instance in data]


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('tour', 'user')

    def validate(self, attrs):
        user = self.context['request'].user
        tour = self.context['view'].get_object()
        if Review.objects.filter(tour=tour, user=user).exists():
            raise serializers.ValidationError('You already reviewed this tour')
        return attrs
