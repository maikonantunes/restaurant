from django.urls import path,include
from rest_framework import routers

from method_of_preparation.views import MethodPreparationViewSet

app_name = 'method_preparation'
router = routers.DefaultRouter()
router.register('method_preparation', MethodPreparationViewSet, basename='method_preparation')
urlpatterns = [
    path('', include(router.urls)),
]
