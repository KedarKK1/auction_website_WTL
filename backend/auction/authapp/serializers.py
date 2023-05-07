from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *


# class UserCreateSerializer(UserCreateSerializer): # Changing the name because swagger is getting confuse betweeh 
# drf_yasg.errors.SwaggerGenerationError: Schema for <class 'djoser.serializers.UserSerializer'> would override distinct serializer <class 'authapp.serializers.UserSerializer'> because they implicitly share the same ref_name; explicitly set the ref_name attribute on both serializers' Meta classes
class UserCreateSerializer2(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        ref_name = "UserCreateSerializer"
        fields = [
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'is_staff',
        ]


# class UserSerializer(UserSerializer):
class UserSerializer2(UserSerializer):
    class Meta(UserSerializer.Meta):
        ref_name = "UserSerializer2"

        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff'
        ]  # don't pass password here
