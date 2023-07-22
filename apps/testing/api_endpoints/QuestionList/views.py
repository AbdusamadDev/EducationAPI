from rest_framework import generics
from apps.testing.api_endpoints.QuestionList.serializers import QuizSerializer
from rest_framework.permissions import IsAuthenticated
from apps.testing.models import Quiz


class QuizQuestionListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_name = self.kwargs.get("subject")
        if category_name is None:
            return Quiz.objects.all()
        return Quiz.objects.filter(category__name=category_name)


__all__ = ['QuizQuestionListView']
