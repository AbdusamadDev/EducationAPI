from rest_framework import serializers

from apps.application.models import Application
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "full_name", "phone", "faculty", "course")


class ApplicationListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Application
        fields = "__all__"
