from rest_framework import serializers
from apps.testing.models import Question, Answer, Quiz


class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "answer_text",)


class QuestionListSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ("id", "title", "answers")

    def get_answers(self, obj):
        return AnswerListSerializer(obj.answers, many=True).data


class QuizSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ("id", "title", "questions")

    def get_questions(self, obj):
        return QuestionListSerializer(obj.question, many=True).data
