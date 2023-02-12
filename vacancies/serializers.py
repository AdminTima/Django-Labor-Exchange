from rest_framework import serializers
from . import models
from resume.serializers import ResumeSerializer
from employers.serializers import EmployerUserSerializer


class VacancySerializer(serializers.ModelSerializer):
    publisher = EmployerUserSerializer(default=serializers.CurrentUserDefault())
    # publisher_id = serializers.PrimaryKeyRelatedField(read_only=True)

    def update(self, instance, validated_data):
        validated_data.pop("publisher", None)
        print(validated_data)
        instance.__dict__.update(validated_data)
        instance.save()
        return instance

    class Meta:
        model = models.Vacancy
        fields = "__all__"


class VacancyResponseSerializer(serializers.ModelSerializer):
    resume = ResumeSerializer(read_only=True)
    resume_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = models.VacancyResponse
        fields = "__all__"


class VacancyDetailSerializer(serializers.ModelSerializer):
    responses = VacancyResponseSerializer(read_only=True, many=True)
    publisher = EmployerUserSerializer(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Vacancy
        fields = "__all__"



