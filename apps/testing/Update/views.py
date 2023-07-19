from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from apps.testing.models import Question, Variation
from apps.testing import serializers


class QuestionEditAPIView(UpdateAPIView):
    model = Question
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = "pk"


class VariationEditAPIView(UpdateAPIView):
    model = Variation
    serializer_class = serializers.VariationSerializer
    queryset = Variation.objects.all()
    # permission_classes = [IsAdminUser]
    lookup_field = "pk"
