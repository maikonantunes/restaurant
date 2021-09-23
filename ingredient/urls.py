from django.urls import path,include
from rest_framework import routers

from ingredient.views import IngredientViewSet

app_name = 'ingredient'

router = routers.DefaultRouter()
router.register('ingredient', IngredientViewSet, basename="ingredient")

urlpatterns = [
    path('', include(router.urls)),
]
