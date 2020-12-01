from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.eats.models import Ingredient
from apps.eats.serializers import IngredientSerializer


class IngredientViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    filter_fields = ('calories', 'name', 'id',)
    permission_classes = [IsAuthenticatedOrReadOnly]
