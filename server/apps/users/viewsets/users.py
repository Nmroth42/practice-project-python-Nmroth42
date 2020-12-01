from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from apps.users.serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.serializers import ModelSerializer


class TokenSerializer(ModelSerializer):

    class Meta:
        model = Token
        fields = ('key',)

token_response = openapi.Response('response description', TokenSerializer)

class UserViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description='Create user auth token',
        responses={201: token_response},
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token = Token.objects.create(user=serializer.instance)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)
