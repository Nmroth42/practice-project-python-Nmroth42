from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('username', 'password',)
        write_only_fields = ('password',)
