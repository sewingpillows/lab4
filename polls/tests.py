from datetime import datetime
from django.test import TestCase
from .models import Question, Choice
from django.utils import timezone
# Create your tests here.
class PollTestCase(TestCase):
    def setUp(self):
        Question.objects.create(
            question_text="test_question?",
            pub_date=timezone.now()
    )

    def test_question_text_valid(self):
        """Question text should work"""
        question = Question.objects.get(
            question_text="test_question?"
        )
        self.assertEqual(
            question.question_text, "test_question?"
        )
