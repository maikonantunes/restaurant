from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
