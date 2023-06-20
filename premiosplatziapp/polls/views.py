from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.

# ## 1° Function Base View creada en esta app
# def index(request):
#     latest_question_list = Question.objects.all() # Traigo todos los objetos pregunta de mi app para renderearlos en mi Template
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     return render(request, "polls/index.html", context) # No es necesario pasar el dict de context expandido como en Flask en Django

# ## 2° View: Nos muestra una pregunta y el detalle de las opciones de respuesta para esa pregunta
# def detail(request, question_id):
#     # question = Question.objects.get(pk=question_id) # Busco solo la question_id que me piden por URL. Si la pregunta no existe vamos a tener un 404 a menos que lo manejemos...
#     question = get_object_or_404(Question, pk=question_id) # Forma segura para buscar un elemento en el modelo
#     context = {
#         "question": question
#     }
#     return render(request, "polls/detail.html", context)


# ## 3° View: Cantidad de votos que tiene cada una de las respuestas de nuestras preguntas
# def results(request, question_id):
#     # Siempre a results vamos a llevar despues de submitear el form en votes
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         "question": question
#     }
#     return render(request, "polls/results.html", context)

# Reformulo mi index view como una generic view que hereda del tipo ListView de Django
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """_summary_
        Return the last five published question
        Returns:
            QuerySet[Any]: _description_
        """
        # return Question.objects.order_by("-pub_date")[:5] # Ordena de las mas recientes a las mas antiguas por el signo menos / Con slices le pido solo 5 registros
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5] # __lte = menor o igual a hoy
    
# Detail view heredada de una Generic View de Django:
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# Result view heredada de una Generic View de Django:
class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

## 4° View: La vamos a usar para votar pero no va a tener un frontend propio.
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) # Con el name choice accedo al value choice.id de la elección del cliente. 
    except (KeyError, Choice.DoesNotExist): # Si llave del dict "choice" no existe...No seleccionó nada
        context= {
            "question": question,
            "error_messege": "No elegiste una respuesta"
        }
        return render(request, "polls/detail.html", context)
    else: # Dentro de un try/except se ejecuta si todo salío bien en el Try
        selected_choice.votes += 1 # Sumo un voto al atributo de Choice
        selected_choice.save() # Salvo los nuevos valores en mi base de datos para luego poder recuperarlos
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,))) # La "," expresa que es una tupla de 1 elemento.
    