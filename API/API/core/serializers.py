from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'phone', 'password')
        read_only_fields = ('count_checkAddr', 'count_checkId', 'count_auth')
        extra_kwargs = {'password': {'write_only': True}}
