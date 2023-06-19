from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

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
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")

## 3° View: Cantidad de votos que tiene cada una de las respuestas de nuestras preguntas
def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta número {question_id}")

## 4° View: La vamos a usar para votar pero no va a tener un frontend propio.
def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta número {question_id}")