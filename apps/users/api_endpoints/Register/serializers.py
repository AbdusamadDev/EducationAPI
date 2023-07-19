from rest_framework import serializers

from apps.users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)

    class Meta:
        model = User
        fields = ("full_name", "phone", "email", "faculty", "course", "password", "password2")

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if password != password2:
            raise serializers.ValidationError({"success": False, "message": "Parol mos kelmadi, qayta urinib ko'ring"})
        return attrs

    def create(self, validated_data):
        del validated_data["password2"]
        return User.objects.create_user(**validated_data)
