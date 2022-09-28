from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q
from .models import UserProfile
from django.utils.http import *
from django.utils.encoding import *
from api.models import UserProfile, Product
from rest_framework import serializers
from icecream import ic


class ProductSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email"]

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)