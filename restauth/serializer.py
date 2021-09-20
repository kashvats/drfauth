from rest_framework import serializers
from .models import school
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class register(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, min_length=4)
    email = serializers.EmailField(max_length=40, min_length=4)
    password = serializers.CharField(max_length=25, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'username already exist'})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'email already exist'})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class school1(serializers.ModelSerializer):
    class Meta:
        model = school
        fields = ['name', 'roll', 'subject', 'city', 'id']
