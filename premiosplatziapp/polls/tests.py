import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

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

    def test_was_published_recently_with_present_question(self):
        """
        was_published_recently, method of Question Model, return
        True for questions whose pub_date is in the present 
        """
        time = timezone.now()
        q = Question(question_text="¿Esta es una pregunta de Test?", pub_date=time)

        self.assertTrue(q.was_published_recently())

    def test_was_published_recently_with_past_question(self):
        """
        was_published_recently, method of Question Model, return
        True for questions whose pub_date is in the past but what his pub_date is greater or equal than today - 1 day.
        """
        time = timezone.now() - datetime.timedelta(hours=6)
        q = Question(question_text="¿Esta es una pregunta de Test?", pub_date=time)

        self.assertEqual(q.was_published_recently(), True)

# Testing de Views: 
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If we haven't got published question the app should print a message with the next content: "No polls are available"
        """
        response = self.client.get(reverse("polls:index")) # Hago una petición HTTP sobre mi url "index" y me guardo la respuesta. 
        #  ¿Que debo verificar? 
        ## 1. Que la respuesta sea satisfactoria. Es decir, StatusCode 200
        self.assertEqual(response.status_code, 200)
        ## 2. Que la respuesta contenga el mensaje "No polls are available"
        self.assertContains(response, "No polls are available")
        ## 3. Que el conjunto de preguntas que trajo Django de sqlite sea una lista vacia
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
        # Los tests deberían pasar exitosamente con el código que tenemos dado que Django Test trabaja con una base de datos provisoria y no con la base de datos que realmente tenemos construida para testear.
    # Challenge: Index ya no muestra preguntas del futuro: 
    def test_no_future_questions(self):
        """
        If we have got question whose pub_date is greater than now the IndexView should not show them
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        questions = response.context["latest_question_list"]
        for question in questions:
            self.assertTrue(question.pub_date <= timezone.now())
    


