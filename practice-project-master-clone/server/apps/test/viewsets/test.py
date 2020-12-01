from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response

from apps.test.models import Test
from apps.test.serializers import TestSerializer


class TestViewSet(RetrieveModelMixin, ListModelMixin, CreateModelMixin, GenericViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    http_method_names = ['get', 'post']

    def get_paginated_response(self, data):
       return Response(data)
