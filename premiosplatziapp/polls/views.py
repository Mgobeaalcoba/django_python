from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

## 1° Function Base View creada en esta app
def index(request):
    latest_question_list = Question.objects.all() # Traigo todos los objetos pregunta de mi app para renderearlos en mi Template
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context) # No es necesario pasar el dict de context expandido como en Flask en Django

## 2° View: Nos muestra una pregunta y el detalle de las opciones de respuesta para esa pregunta
def detail(request, question_id):
    # question = Question.objects.get(pk=question_id) # Busco solo la question_id que me piden por URL. Si la pregunta no existe vamos a tener un 404 a menos que lo manejemos...
    question = get_object_or_404(Question, pk=question_id) # Forma segura para buscar un elemento en el modelo
    context = {
        "question": question
    }
    return render(request, "polls/detail.html", context)


## 3° View: Cantidad de votos que tiene cada una de las respuestas de nuestras preguntas
def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta número {question_id}")

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
    