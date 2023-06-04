from django.core.exceptions import ValidationError
from django.db import models


class Favorite(models.Model):
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='favorites', blank=True, null=True)
    clothing = models.ForeignKey(
        'clothes.Clothing', on_delete=models.CASCADE, blank=True, null=True)
    food = models.ForeignKey(
        'food.Food', on_delete=models.CASCADE, blank=True, null=True)
    souvenir = models.ForeignKey(
        'souvenirs.Souvenir', on_delete=models.CASCADE, blank=True, null=True)
    tour = models.ForeignKey(
        'tours.Tour', on_delete=models.CASCADE, blank=True, null=True)

    def clean(self):
        fields = ['food', 'clothing', 'tour', 'souvenir']
        count = sum(getattr(self, field) is not None for field in fields)

        if count == 0:
            raise ValidationError("At least one field should be selected.")
        elif count > 1:
            raise ValidationError("Only one field should be selected.")
