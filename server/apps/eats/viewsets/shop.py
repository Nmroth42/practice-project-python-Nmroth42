from rest_framework.viewsets import ModelViewSet
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from apps.eats.models import Shop
from apps.eats.serializers import ShopSerializer
from apps.main.permissions import ShopPermission


class ShopViewSet(ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    filter_fields = (
        'owner_id',
        'name',
        'work_start',
        'work_end',
        'addres',
        'latitude',
        'longitude',
        'average_dish_cost'
    )
    permission_classes = [ShopPermission]

    @method_decorator(cache_page(60*15))
    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)
