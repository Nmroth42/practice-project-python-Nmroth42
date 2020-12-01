from rest_framework.serializers import ModelSerializer

from apps.test.models import Test


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = ('name', 'random_string', 'id')
        extra_kwargs = {'random_string': {'read_only': True}}
