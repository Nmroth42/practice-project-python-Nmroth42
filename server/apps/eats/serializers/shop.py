from django.conf import settings
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.eats.models import Shop
from yandex_geocoder import Client

client = Client(settings.YANDEX_GEOCODER_KEY)


class ShopSerializer(ModelSerializer):
    owner_id = serializers.IntegerField(source='owner.id', read_only=True)
    class Meta:
        model = Shop
        exclude = ['owner']
        read_only_fields = ('latitude', 'longitude','average_dish_cost')

    def create(self, validated_data):
        shop = Shop(**validated_data)
        shop.owner = self.context['request'].user
        client = Client(settings.YANDEX_GEOCODER_KEY)
        shop.latitude, shop.longitude = client.coordinates(shop.addres)
        shop.save()
        return shop

    def get_average_dish_cost(self, instance):
        pass
