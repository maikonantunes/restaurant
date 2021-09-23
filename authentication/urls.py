from django.urls import path, include
from rest_framework import routers

from authentication.views import LoginViewSet

app_name = 'authentication'

router = routers.DefaultRouter()
router.register('login', LoginViewSet, basename="login")

urlpatterns = [
    path('', include(router.urls)),
]
