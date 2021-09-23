from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from method_of_preparation.models import MethodPreparation
from method_of_preparation.serializers import MethodPreparationSerializer


class MethodPreparationViewSet(viewsets.ModelViewSet):
    queryset = MethodPreparation.objects.all()
    serializer_class = MethodPreparationSerializer
    permission_classes = [IsAuthenticated]



