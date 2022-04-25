from dataclasses import field
from msilib.schema import tables
from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from requests import request
from rest_framework import serializers
from sampleapp.models import Book,B2CUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import check_password





##Model Serilaizer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(required=True)
    def validate(self, validated_data):
        user=B2CUser.objects.filter(email=validated_data["email"])
        if not user.exists():
            raise serializers.ValidationError({"email":"Email Not Found"})
        if not check_password(validated_data["password"],user.first().password):
            raise serializers.ValidationError({"password":"In correct Password"})
        return validated_data
    
#Custom serializer 
class RegisterSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True,
                                 validators=[UniqueValidator(queryset=B2CUser.objects.all())])
    password=serializers.CharField(required=True,min_length=8,write_only=True)
    name=serializers.CharField(required=True,max_length=50)
    contact=serializers.CharField(max_length=10)
    def create(self,validated_data):
        try:
            user=B2CUser.objects.get(email=validated_data["email"],name=validated_data["name"])
            if user:
                user.delete()
        except B2CUser.DoesNotExist:
            user=B2CUser.objects.create_user(**validated_data)
            return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=B2CUser
        fields='__all__'
