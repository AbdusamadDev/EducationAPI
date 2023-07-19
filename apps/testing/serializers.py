from rest_framework import serializers
from rest_framework.response import Response

from apps.testing.models import (
    TestResultModel,
    Question,
    Variation,
    Subject
)

class QuestionAndChoiceSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    choice = serializers.IntegerField()

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    subject_id = SubjectSerializer().data

    class Meta:
        model = Question
        fields = ["text", "subject_id"]

class TestSerializer(serializers.ModelSerializer):
    questions = QuestionAndChoiceSerializer(many=True)

    class Meta:
        model = TestResultModel
        fields = ["user_id", "subject_id", "questions"]

class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = '__all__'
