from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.testing.models import Category, Question, Quiz, TestResult


User = get_user_model()


class TestProductView(APITestCase):
    def setUp(self):
        self.user = User.objects.create(full_name="Samandar", phone="+998913665113")
        self.category = Category.objects.create(name="Matematika")
        self.quiz = Quiz.objects.create(category=self.category, title="1-semester")
        self.question = Question.objects.create(title="1+1= ?", quiz=self.quiz)
        self.test_result = TestResult.objects.create(user=self.user, quiz=self.quiz, score=15)
        self.category_2 = Category.objects.create(name="Matematika_2")
        self.quiz_2 = Quiz.objects.create(category=self.category_2, title="2-semester")

    def test_quiz_list_already_solved(self):
        url = reverse("quiz-question-list")
        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}",
        }
        response = self.client.get(f"{url}?subject={self.quiz.category.name}", **headers)
        assert response.status_code == 403
        assert response.json()["detail"] == "У вас недостаточно прав для выполнения данного действия."

    def test_quiz_list(self):
        url = reverse("quiz-question-list")
        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}",
        }
        response = self.client.get(f"{url}?subject={self.quiz_2.category.name}", **headers)
        assert response.status_code == 200
        assert response.json()[0]["id"] == self.quiz_2.id
        assert response.json()[0]["title"] == self.quiz_2.title
