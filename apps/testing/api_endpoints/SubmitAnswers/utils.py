from apps.testing.models import Answer


def calculate_quiz_score(quiz, user_answers):
    total_questions = quiz.question.count()
    correct_answers = 0

    for question in quiz.question.all():
        user_answer = user_answers.get(str(question.id), None)

        if user_answer is not None:
            if Answer.objects.filter(id=user_answer, question=question, is_correct=True).exists():
                correct_answers += 1

    # Calculate the score as a percentage of correct answers
    return correct_answers, total_questions
