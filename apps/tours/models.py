from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class TourCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='tours')
    category = models.ForeignKey(TourCategory, on_delete=models.CASCADE)
    season = models
    time = models.IntegerField()
    distance = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    comment = models.TextField()
    stars = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.stars
