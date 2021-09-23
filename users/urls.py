from django.urls import path,include
from rest_framework import routers


from users.views import ChefViewSet,ClientViewSet

app_name = 'users'
router = routers.DefaultRouter()
router.register('chef', ChefViewSet, basename='chef'),
router.register('search_food', ClientViewSet, basename='search_food'),


urlpatterns = [
    path('', include(router.urls)),
]
