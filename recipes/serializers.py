from rest_framework import serializers

from ingredient.serializers import IngredientSerializer
from method_of_preparation.serializers import MethodPreparationSerializer
from recipes.models import Recipes


class RecipesSerializer(serializers.ModelSerializer):
    ingredient_obj = serializers.SerializerMethodField()
    method_preparation_obj = serializers.SerializerMethodField()

    def get_ingredient_obj(self, obj):
        try:
            ingredient_objs = IngredientSerializer(obj.ingredient, many=True)
            return ingredient_objs.data
        except Exception as e:
            return []

    def get_method_preparation_obj(self, obj):
        try:
            method_preparation_objs = MethodPreparationSerializer(obj.method_preparation, many=True)
            return method_preparation_objs.data
        except Exception as e:
            return []

    class Meta:
        model = Recipes
        fields = '__all__'

