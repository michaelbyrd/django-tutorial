import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Question

def create_question(question_text, days):
    """
    Creates a question with the given 'question_text' published the given number
    of 'dats' offet to now (negative for questions published in the past,
    positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        # time = timezone.now() + datetime.timedelta(days=30)
        # future_question = Question(pub_date=time)
        future_question = create_question( "not much to ask", 30)
        result = future_question.was_published_recently()
        self.assertEqual(result, False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older that 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        result = old_question.was_published_recently()
        self.assertEqual(result, False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose pub_date
        is with the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        result = recent_question.was_published_recently()
        self.assertEqual(result, True)
