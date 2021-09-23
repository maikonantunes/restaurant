from django.db import models
from ingredient.models import Ingredient
from method_of_preparation.models import MethodPreparation
from authentication.models import User


class Recipes (models.Model):
    name = models.CharField(max_length=150, null=True, blank=True,)
    description = models.TextField(null=True, blank=True,)
    image_food = models.ImageField(null=True, blank=True,)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)
    ingredient = models.ManyToManyField(Ingredient, null=True, blank=True,)
    method_preparation = models.ManyToManyField(MethodPreparation, null=True, blank=True,)

    def __str__(self):
        return self.name

