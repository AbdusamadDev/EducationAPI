from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.users.models import User
from apps.testing.models import TestResult, Quiz, Question, Answer, Category


class QuizTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(phone="+998913665113", full_name="Samandar")
        self.category = Category.objects.create(name="Matematika")
        self.quiz = Quiz.objects.create(title='Test Quiz', category=self.category)

        # Create two questions for the quiz
        self.question1 = Question.objects.create(quiz=self.quiz, title='Question 1')
        self.question2 = Question.objects.create(quiz=self.quiz, title='Question 2')

        # Create answers for the questions (Assuming the first answer is correct for both questions)
        self.answer1_1_correct = Answer.objects.create(question=self.question1, answer_text='Answer 1-1', is_correct=True)
        self.answer1_2 = Answer.objects.create(question=self.question1, answer_text='Answer 1-2')
        self.answer2_1_correct = Answer.objects.create(question=self.question2, answer_text='Answer 2-1', is_correct=True)
        self.answer2_2 = Answer.objects.create(question=self.question2, answer_text='Answer 2-2')

    def test_submit_quiz_answers(self):
        quiz = Quiz.objects.first()  # Assuming you have already created a quiz in the setUp method
        questions = quiz.question.all()

        # Prepare user's answers with question IDs and answer IDs
        user_answers = {
            self.question1.id: self.answer1_2.id,  # Choose the incorrect answer
            self.question2.id: self.answer2_1_correct.id,   # Choose the correct answer
        }

        # Prepare the data to be sent in the request
        data = {
            "quiz_id": quiz.id,
            "user_answers": user_answers,
        }

        url = reverse("submit-answers")  # Replace with the actual URL name for your view
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.user.tokens.get('access')}"}
        response = self.client.post(url, data, format="json", **headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Retrieve the TestResult instance from the response data
        test_result = TestResult.objects.get(id=response.data["result_id"])
        self.assertEqual(test_result.user, self.user)
        self.assertEqual(test_result.quiz, quiz)
        self.assertEqual(test_result.score, 1)

