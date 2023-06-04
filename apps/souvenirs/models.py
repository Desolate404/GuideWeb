from django.db import models


class SouvenirCategory(models.Model):
    name = models.CharField(max_length=128)


class Souvenir(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='souvenir/')
    category = models.ForeignKey(SouvenirCategory, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
