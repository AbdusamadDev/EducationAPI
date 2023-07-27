from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.testing.api_endpoints.QuestionList.serializers import QuizSerializer
from apps.testing.models import Quiz

from .permission import NotSolvedBefore


class QuizQuestionListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated & NotSolvedBefore]

    def get_queryset(self):
        category_name = self.request.query_params.get("subject")
        if category_name is None:
            return Quiz.objects.none()
        return Quiz.objects.filter(category__name=category_name)


__all__ = ["QuizQuestionListView"]
