from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from recipes.models import Recipes
from recipes.serializers import RecipesSerializer
from recipes.views import RecipesViewSet


class ChefViewSet(RecipesViewSet):
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        recipes = Recipes.objects.filter(user=request.user
                                         ).order_by('-id')

        page = self.paginate_queryset(recipes)
        if page is not None:
            serializer = RecipesSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = RecipesSerializer(recipes, many=True)
            return Response(serializer.data)


class ClientViewSet(RecipesViewSet):
    http_method_names = ['get']

