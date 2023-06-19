import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

# Generalmente vamos a testear Modelos ó Vistas

## Testing de Models: 
class QuestionModelTest(TestCase):
    ### Creamos un método por cada Test a ejecutar
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently returns False for questions whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        q = Question(question_text="¿Esta es una pregunta de Test?", pub_date=time)

        self.assertIs(q.was_published_recently(), False)


