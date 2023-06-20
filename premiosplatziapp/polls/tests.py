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
def create_question(question_text: str, days: int, tag_choice: bool):
    """Create a question with the given "question_text", and published the given number of days offset to now (negative for questions published in the past, positive for question that have yet to be published)

    Args:
        question_text (str): The text of de question
        days (int): The delta days with now 
    
    Return:
        A Question object
    """
    time = timezone.now() + datetime.timedelta(days=days)
    question = Question.objects.create(question_text=question_text, pub_date=time)
    if tag_choice:
        question.choice_set.create(choice_text="opcion 1", votes=0)
        question.choice_set.create(choice_text="opcion 2", votes=0)

    return question


# Testing de Views:
## Tests para Index View: 
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
        q1 = create_question("pregunta 1", -1, True)
        q2 = create_question("pregunta 2", -10, True)
        q3 = create_question("pregunta 3 - Futuro", 15, True)
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
        create_question("Future question", 30, True) # Creo una pregunta del fúturo en nuestra base de datos de testing
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available") # Compruebo que, como la pregunta es del fúturo y es la única, no se muestra ninguna en mi index. 
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the index page. 
        """
        question = create_question("Future question", -10, True) 
        response = self.client.get(reverse("polls:index")) 
        self.assertQuerysetEqual(response.context["latest_question_list"], [question]) # Verificamos que la lista que nos devuelve la consulta con los datos contenga a la pregunta que generamos arriba

    def test_future_question_and_past_question(self):
        """
        When we publish a question from the future and a question from the past, it should only show the one from the past
        """
        past_question = create_question("pregunta 2", -10, True)
        future_question = create_question("pregunta 3 - Futuro", 15, True)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question])
    
    def test_two_past_questions(self):
        """
        When we publish two questions from the past, it should show twice questions. 
        """
        past_question_1 = create_question("pregunta 2", -10, True)
        past_question_2 = create_question("pregunta 3 - Futuro", -15, True)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question_1, past_question_2])

    def test_question_without_choice(self):
        """
        When we publish one question without choice, it should not show
        """
        # Pregunta sin respuesta que no debería mostrarse
        question = create_question("pregunta 2", -10, False)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
        self.assertContains(response, "No polls are available")

    def test_question_with_choice(self):
        """
        When we publish one question with choice, it should not show
        """
        # Pregunta con respuesta que si debería mostrarse
        question = create_question("pregunta 2", -10, True)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
        self.assertEqual(response.status_code, 200)


## Test para Detail Views
class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future returns a 404 error not found
        """
        future_question = create_question("pregunta 3 - Futuro", 15, True)
        url = reverse("polls:detail", args=(future_question.id,)) # id y pk para django son lo mismo. 
        response = self.client.get(url)
        # Verifico que una petición HTTP a la URL definida arriba, que trae el detalle de una pregunta del futuro, me devuelva un 404 y no un 200
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past displays the question´s text. 
        """
        past_question_1 = create_question("pregunta 2", -10, True)
        url = reverse("polls:detail", args=(past_question_1.id,))
        response = self.client.get(url)
        # Verifico que una petición HTTP a la URL definida arriba, que trae el detalle de una pregunta del pasado, me duvuelva un 200 y no un 404
        self.assertEqual(response.status_code, 200)
        # Verifico que en la respuesta a mi request exista el texto que forma parte de mi Question. 
        self.assertContains(response, past_question_1.question_text)

    def test_question_without_choice(self):
        """
        When we publish one question without choice, it should not show
        """
        # Pregunta sin respuesta que no debería mostrarse
        question = create_question("pregunta 2", -10, False)
        url = reverse("polls:detail", args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_question_with_choice(self):
        """
        When we publish one question with choice, it should not show
        """
        # Pregunta con respuesta que si debería mostrarse
        question = create_question("pregunta 2", -10, True)
        url = reverse("polls:detail", args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question.question_text)

## Challenge Final 1: 
## Tests para Results View: 
class QuestionResultViewTest(TestCase):
    def test_future_question_results(self):
        """
        The results view of a question with a pub_date in the future returns a 404 error not found
        """
        future_question = create_question("pregunta 3 - Futuro", 15, True)
        url = reverse("polls:results", args=(future_question.id,)) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question_results(self):
        """
        The results view of a question with a pub_date in the past displays the question's text. 
        """
        past_question_1 = create_question("pregunta 2", -10, True)
        url = reverse("polls:results", args=(past_question_1.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_question_1.question_text)

    def test_question_without_choice(self):
        """
        When we publish one question without choice, it should not show
        """
        # Pregunta sin respuesta que no debería mostrarse
        question = create_question("pregunta 2", -10, False)
        url = reverse("polls:results", args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_question_with_choice(self):
        """
        When we publish one question with choice, it should not show
        """
        # Pregunta con respuesta que si debería mostrarse
        question = create_question("pregunta 2", -10, True)
        url = reverse("polls:results", args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question.question_text)
