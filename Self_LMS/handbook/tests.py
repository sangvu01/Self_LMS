from django.test import TestCase
from django.urls import reverse

from .models import Choice, Course, Question, Quiz, QuizAttempt, QuizAttemptAnswer
from .quiz_service import calculate_attempt_result


class QuizModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            slug="test-course",
            title="Test Course",
            description="A test course",
            duration="2 weeks",
            level="beginner",
        )
        self.quiz = Quiz.objects.create(
            course=self.course,
            title="Test Quiz",
            description="A test quiz",
            is_active=True,
        )

    def test_quiz_can_have_questions_and_choices(self):
        question = Question.objects.create(quiz=self.quiz, text="What is 2 + 2?", order=1)
        Choice.objects.create(question=question, text="3", is_correct=False)
        correct_choice = Choice.objects.create(question=question, text="4", is_correct=True)

        self.assertEqual(self.quiz.questions.count(), 1)
        self.assertEqual(question.choices.count(), 2)
        self.assertEqual(question.correct_choice, correct_choice)

    def test_quiz_can_be_created_for_a_course(self):
        self.assertEqual(self.course.quizzes.count(), 1)
        self.assertEqual(self.quiz.course, self.course)

    def test_calculate_attempt_result_scores_correct_answers(self):
        question = Question.objects.create(quiz=self.quiz, text="What is 2 + 2?", order=1)
        correct_choice = Choice.objects.create(question=question, text="4", is_correct=True)
        Choice.objects.create(question=question, text="5", is_correct=False)

        result = calculate_attempt_result(
            questions=[question],
            selected_answers={question.id: correct_choice.id},
        )

        self.assertEqual(result["correct"], 1)
        self.assertEqual(result["total"], 1)
        self.assertEqual(result["score"], 100)
        self.assertTrue(result["review"][0]["is_correct"])

    def test_empty_quiz_redirects_to_start_page(self):
        response = self.client.get(
            reverse("quiz_detail", kwargs={"course_slug": self.course.slug, "quiz_id": 1})
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("start_quiz", kwargs={"course_slug": self.course.slug}))

    def test_course_list_api_includes_quiz_question_count(self):
        question = Question.objects.create(quiz=self.quiz, text="Sample question", order=1)
        Choice.objects.create(question=question, text="A", is_correct=True)

        response = self.client.get(reverse("api-courses"))

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["quiz_count"], 1)

    def test_second_question_page_uses_question_position_not_quiz_id(self):
        first_question = Question.objects.create(quiz=self.quiz, text="First question", order=1)
        Choice.objects.create(question=first_question, text="A", is_correct=True)
        second_question = Question.objects.create(quiz=self.quiz, text="Second question", order=2)
        Choice.objects.create(question=second_question, text="B", is_correct=True)

        self.client.session[f"quiz_order_{self.quiz.id}"] = [first_question.id, second_question.id]
        self.client.session.save()

        response = self.client.get(
            reverse("quiz_detail", kwargs={"course_slug": self.course.slug, "quiz_id": 2})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Second question")

    def test_course_detail_api_returns_latest_three_attempts_with_correct_counts(self):
        first_question = Question.objects.create(quiz=self.quiz, text="First question", order=1)
        first_correct = Choice.objects.create(question=first_question, text="A", is_correct=True)
        Choice.objects.create(question=first_question, text="B", is_correct=False)

        second_question = Question.objects.create(quiz=self.quiz, text="Second question", order=2)
        second_correct = Choice.objects.create(question=second_question, text="C", is_correct=True)
        Choice.objects.create(question=second_question, text="D", is_correct=False)

        for _ in range(4):
            attempt = QuizAttempt.objects.create(quiz=self.quiz, score=100, total_questions=2)
            QuizAttemptAnswer.objects.create(attempt=attempt, question=first_question, selected_choice=first_correct, is_correct=True)
            QuizAttemptAnswer.objects.create(attempt=attempt, question=second_question, selected_choice=second_correct, is_correct=True)

        response = self.client.get(
            reverse("api-courses-id", kwargs={"course_slug": self.course.slug})
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data["recent_attempts"]), 3)
        self.assertGreaterEqual(data["recent_attempts"][0]["correct_answers"], 0)
