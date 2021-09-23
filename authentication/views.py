from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from authentication.serializers import UserSerializer


class LoginViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'],
                                password=serializer.validated_data['password'])
            if not user:
                return Response({'error': 'Usuário ou senha errados'},
                                status=HTTP_404_NOT_FOUND)
            token = Token.objects.get_or_create(user=user)
            return Response({'token': token[0].key},
                            status=HTTP_200_OK)
        return Response({'erro': 'Por favor digite seu usuário ou sua senha'},
                        status=HTTP_400_BAD_REQUEST)
