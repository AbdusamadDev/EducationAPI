from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.testing.api_endpoints.SubmitAnswers.utils import calculate_quiz_score
from apps.testing.models import Quiz, TestResult


class SubmitAnswersView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Assuming the user sends the answers as a dictionary with question IDs as keys and answer IDs as values
        user_answers = request.data.get("user_answers", {})
        quiz_id = request.data.get("quiz_id")

        try:
            quiz = Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            return Response({"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)

        score, total_questions = calculate_quiz_score(quiz, user_answers)

        # Create the TestResult instance and save it
        test_result = TestResult.objects.create(user=request.user, quiz=quiz, score=score)

        return Response(
            {"score": score, "total_questions": total_questions, "result_id": test_result.id},
            status=status.HTTP_201_CREATED,
        )


__all__ = ["SubmitAnswersView"]
