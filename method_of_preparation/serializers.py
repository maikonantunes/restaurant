from rest_framework import serializers
from method_of_preparation.models import MethodPreparation


class MethodPreparationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MethodPreparation
        fields = '__all__'