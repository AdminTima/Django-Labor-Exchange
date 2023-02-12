from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.serializers import RegisterUserSerializer, UpdateUserSerializer
from . import models

User = get_user_model()


class RegisterEmployerSerializer(RegisterUserSerializer):
    company_name = serializers.CharField(max_length=120)
    company_description = serializers.CharField()

    def create(self, validated_data: dict):
        user = super().create(validated_data)
        try:
            return models.Employer.objects.create(
                company_name=validated_data["company_name"],
                company_description=validated_data["company_description"],
                user=user,
            )
        except Exception as err:
            print(err)
            user.delete()


class EmployerSerializer(UpdateUserSerializer):
    id = serializers.UUIDField(read_only=True)
    company_name = serializers.CharField()
    company_description = serializers.CharField()

    def update(self, instance, validated_data):
        super().update(instance.user, validated_data)
        instance.company_name = validated_data["company_name"]
        instance.company_description = validated_data["company_description"]
        instance.save()
        return instance


class EmployerUserSerializer(serializers.ModelSerializer):
    employer = EmployerSerializer(read_only=True)

    class Meta:
        model = User
        fields = ("email", "id", "employer")


