from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.testing.models import (
    Question,
    Subject,
    TestResultModel,
    Variation
)

class QuestionDeleteAPIView(DestroyAPIView):
    """Delete Questions of the subject when is needed"""

    model = Question
    queryset = Question.objects.all()
    # permission_classes = [IsAdminUser]
    lookup_field = "pk"

class SubjectDeleteAPIView(DestroyAPIView):
    """Delete Subjects when is needed"""

    model = Subject
    queryset = Subject.objects.all()
    lookup_field = "pk"
    # permission_classes = [IsAdminUser]

class TestResultDeleteAPIView(DestroyAPIView):
    """Delete data from results"""

    model = TestResultModel
    queryset = TestResultModel.objects.all()
    lookup_field = "pk"
    # permission_classes = [IsAdminUser]

class VariationDeleteAPIView(DestroyAPIView):
    model = Variation
    queryset = Variation.objects.all()
    lookup_field = "pk"
