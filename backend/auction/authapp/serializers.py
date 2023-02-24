from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = [
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'is_staff',
        ]


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff'
        ]  # don't pass password here
