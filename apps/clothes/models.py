from django.db import models


class ClothingCategory(models.Model):
    name = models.CharField(max_length=128)


class Clothing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='clothes/')
    category = models.ForeignKey(ClothingCategory, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
