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

# Función auxiliar para testear preguntas del pasado y del futuro:
def create_question(question_text, days):
    """Create a question with the given "question_text", and published the given number of days offset to now (negative for questions published in the past, positive for question that have yet to be published)

    Args:
        question_text (str): The text of de question
        days (int): The delta days with now 
    
    Return:
        A Question object
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

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
        q1 = create_question("pregunta 1", days=-1)
        q2 = create_question("pregunta 2", days=-10)
        q3 = create_question("pregunta 3 - Futuro", days=15)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        questions = response.context["latest_question_list"]
        for question in questions:
            self.assertTrue(question.pub_date <= timezone.now())
        self.assertQuerysetEqual(response.context["latest_question_list"], [q1,q2])

    # Mismo test de arriba pero con solución alternativa: 
    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on the index page. 
        """
        create_question("Future question", days=30) # Creo una pregunta del fúturo en nuestra base de datos de testing
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available") # Compruebo que, como la pregunta es del fúturo y es la única, no se muestra ninguna en mi index. 
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the index page. 
        """
        question = create_question("Future question", -10) # Creo una pregunta del fúturo en nuestra base de datos de testing
        response = self.client.get(reverse("polls:index")) 
        self.assertQuerysetEqual(response.context["latest_question_list"], [question]) # Verificamos que la lista que nos devuelve la consulta con los datos contenga a la pregunta que generamos arriba

    def test_future_question_and_past_question(self):
        """
        When we publish a question from the future and a question from the past, it should only show the one from the past
        """
        past_question = create_question("pregunta 2", days=-10)
        future_question = create_question("pregunta 3 - Futuro", days=15)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question])
    
    def test_two_past_questions(self):
        """
        When we publish two questions from the past, it should show twice questions. 
        """
        past_question_1 = create_question("pregunta 2", days=-10)
        past_question_2 = create_question("pregunta 3 - Futuro", days=-15)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question_1, past_question_2])
