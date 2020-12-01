from rest_framework.serializers import ModelSerializer

from apps.eats.models import Ingredient


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('calories', 'name', 'id')
