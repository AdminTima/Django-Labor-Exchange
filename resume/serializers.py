from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"
