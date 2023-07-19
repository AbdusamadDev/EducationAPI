from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.testing.models import (
    Question,
    TestResultModel,
    Subject,
    Variation
)
from apps.testing.List.serializers import (
    TestSerializer,
    QuestionSerializer,
    SubjectSerializer,
    VariationSerializer
)


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all().order_by("?")

    def get_queryset(self):
        subject_pk = self.request.query_params.get("id")  # Retrieve the subject_pk from URL kwargs
        queryset = super().get_queryset()
        if subject_pk:
            queryset = queryset.filter(subject_id=subject_pk)  # Filter queryset based on subject_pk
            # return queryset

        
        return queryset

class TestResultListAPIView(ListAPIView):
    model = TestResultModel
    queryset = TestResultModel.objects.all()
    serializer_class = TestSerializer
    # permission_classes = [IsAdminUser]

class SubjectListAPIView(ListAPIView):
    model = Subject
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = [IsAdminUser]

class VariationListAPIView(ListAPIView):
    model = Variation
    queryset = Variation.objects.all().order_by("?")
    serializer_class = VariationSerializer
    # permission_classes = [IsAdminUser]

    def get_queryset(self):
        pk = self.kwargs.get('pk')  # Retrieve the subject_pk from URL kwargs
        queryset = super().get_queryset()
        queryset = queryset.filter(question_id=pk)  # Filter queryset based on subject_pk
        return queryset
