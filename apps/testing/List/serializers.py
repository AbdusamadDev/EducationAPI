from rest_framework import serializers

from apps.users.api_endpoints.Register.serializers import UserCreateSerializer
from apps.testing.models import (
    TestResultModel,
    Question,
    Variation,
    Subject
)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    user_id = UserCreateSerializer()

    class Meta:
        model = TestResultModel
        fields = ["user_id", "result"]

class QuestionSerializer(serializers.ModelSerializer):
    subject_id = SubjectSerializer()

    class Meta:
        model = Question
        fields = ["id", "text", "subject_id"]

class VariationSerializer(serializers.ModelSerializer):
    question_id = QuestionSerializer()

    class Meta:
        model = Variation
        fields = '__all__'
        