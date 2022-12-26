from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvUser
        fields = ['username', 'email', 'avatar']


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvUser
        fields = ['username', 'email', 'password', 'avatar']

    def create(self, validated_data):
        user = AdvUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            avatar=validated_data['avatar']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'image']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product']
