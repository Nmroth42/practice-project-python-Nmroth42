from rest_framework.serializers import ModelSerializer

from apps.eats.models import Dish


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            'id',
            'name',
            'image',
            'price',
            'shop',
            'ingredients',
            'calories_sum'
        )
        extra_kwargs = {'calories_sum': {'read_only': True}}
