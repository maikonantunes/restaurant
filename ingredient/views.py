from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ingredient.models import Ingredient
from ingredient.serializers import IngredientSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]

