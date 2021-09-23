from django.db import models


class Ingredient(models.Model):

    quantity = models.IntegerField()
    description = models.TextField()
    order_ingredient = models.IntegerField()

    def __str__(self):
        return self.description
