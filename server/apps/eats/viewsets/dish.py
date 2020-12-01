from rest_framework.viewsets import ModelViewSet

from apps.eats.models import Dish
from apps.eats.serializers import DishSerializer
from apps.main.permissions import DishPermission


class DishViewSet(ModelViewSet):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()
    filter_fields = ('id', 'name', 'price', 'shop', 'ingredients',)
    permission_classes = [DishPermission]
