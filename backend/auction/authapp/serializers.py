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
            'usertype',
        ]


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'usertype'
        ]  # don't pass password here
