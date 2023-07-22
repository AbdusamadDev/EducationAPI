from rest_framework import generics
from apps.testing.api_endpoints.QuestionList.serializers import QuestionListSerializer
from rest_framework.permissions import IsAuthenticated
from apps.testing.models import Question


class QuizQuestionListView(generics.ListAPIView):
    serializer_class = QuestionListSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_name = self.kwargs.get("subject")
        if category_name is None:
            return Question.objects.all()
        return Question.objects.filter(quiz__category__name=category_name)


__all__ = ['QuizQuestionListView']
