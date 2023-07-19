from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveAPIView

from apps.testing.models import (
    TestResultModel,
    Variation,
    Subject,
    Question
)
from apps.testing.Details.serializers import (
    TestSerializer,
    SubjectSerializer,
    VariationSerializer,
    QuestionSerializer
)

class TestResultRetrieveAPIView(RetrieveAPIView):
    model = TestResultModel
    serializer_class = TestSerializer
    lookup_field = "pk"
    queryset = TestResultModel.objects.all()
    # permission_classes = [IsAdminUser]

class VariationRetrieveAPIView(RetrieveAPIView):
    model = Variation
    serializer_class = VariationSerializer
    lookup_field = "pk"
    queryset = Variation.objects.all()

class SubjectRetrieveAPIView(RetrieveAPIView):
    model = Subject
    serializer_class = SubjectSerializer
    lookup_field = "pk"
    queryset = Subject.objects.all()

class QuestionRetrieveAPIView(RetrieveAPIView):
    model = Question
    serializer_class = QuestionSerializer
    lookup_field = "pk"
    queryset = Question.objects.all()
