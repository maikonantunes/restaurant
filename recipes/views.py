from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from recipes.models import Recipes
from recipes.serializers import RecipesSerializer


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    search_fields = ['name', 'description', 'ingredient__description', 'user__name']

    class ActionBasedPermission(AllowAny):

        def has_permission(self, request, view):
            for klass, actions in getattr(view, 'action_permissions', {}).items():
                if view.action in actions:
                    return klass().has_permission(request, view)
            return False

    permission_classes = [ActionBasedPermission]
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'create'],
        AllowAny: ['retrieve', 'get', 'list']
    }



