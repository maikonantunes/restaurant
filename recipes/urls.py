from django.urls import path, include
from rest_framework import routers

from recipes.views import RecipesViewSet

app_name = 'recipes'
router = routers.DefaultRouter()
router.register('recipes', RecipesViewSet, basename='recipes'),


urlpatterns = [
    path('', include(router.urls)),
]
