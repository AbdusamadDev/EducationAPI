from django.urls import path
from apps.testing.api_endpoints import QuizQuestionListView, SubmitAnswersView


urlpatterns = [
    path("", QuizQuestionListView.as_view(), name="quiz-question-list"),
    path("submit/", SubmitAnswersView.as_view(), name="submit-answers"),
]
