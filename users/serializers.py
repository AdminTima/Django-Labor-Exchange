from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


User = get_user_model()


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        write_only=True
    )
    password = serializers.CharField(write_only=True, validators=[validate_password])

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"]
        )


class UpdateUserSerializer(serializers.Serializer):

    email = serializers.EmailField(write_only=True)

    def update(self, instance, validated_data):
        if instance.email != validated_data["email"]:
            instance.email = validated_data["email"]
            instance.save()
        return instance

