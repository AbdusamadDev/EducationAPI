from rest_framework import serializers

from apps.testing.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
        )
