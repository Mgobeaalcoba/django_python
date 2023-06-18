from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

## 1° Function Base View creada en esta app
def index(request):
    return HttpResponse("Estás en la página principal de Premios Platzi App")

## 2° View: Nos muestra una pregunta y el detalle de las opciones de respuesta para esa pregunta
def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")

## 3° View: Cantidad de votos que tiene cada una de las respuestas de nuestras preguntas
def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta número {question_id}")

## 4° View: La vamos a usar para votar pero no va a tener un frontend propio.
def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta número {question_id}")