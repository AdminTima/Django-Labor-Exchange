from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.serializers import RegisterUserSerializer
from .models import Employee
from users.serializers import UpdateUserSerializer

User = get_user_model()


class RegisterEmployeeSerializer(RegisterUserSerializer):
    id = serializers.UUIDField(read_only=True)
    close_profile = serializers.BooleanField(default=False)
    in_active_search = serializers.BooleanField(default=True)

    def create(self, validated_data):
        user = super().create(validated_data)
        try:
            return Employee.objects.create(user=user)
        except Exception as err:
            print(err)
            user.delete()

    def update(self, instance, validated_data):
        super().update(instance.user, validated_data)
        instance.close_profile = validated_data["close_profile"]
        instance.in_active_search = validated_data["in_active_search"]
        instance.save()
        return instance


class EmployeeSerializer(UpdateUserSerializer):
    id = serializers.UUIDField()
    close_profile = serializers.BooleanField(default=False)
    in_active_search = serializers.BooleanField(default=True)

    def update(self, instance, validated_data):
        super().update(instance.user, validated_data)
        instance.close_profile = validated_data["close_profile"]
        instance.in_active_search = validated_data["in_active_search"]
        instance.save()
        return instance


class EmployeeUserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = User
        fields = ("email", "id", "employee")

