from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# Config para que en el mismo formulario donde creo preguntas me aparezca la opción para crear respuestas:
class ChoiceInline(admin.StackedInline):
    model = Choice
    # Cuantas respuestas quiero agregar por default: 
    extra = 3 # Spoiler: Si no uso las tres puedo eliminarlas en el form directamente

# Las clases que creemos con el nombre de un modelo y la palabra admin al final nos van a servir para configurar como queremos ver al modelo en el Admin
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        "pub_date", 
        "question_text"
    ]
    # Agrego dentro de mi clase Question a Choice como una clase dependiente y necesaria para generar la Question. 
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
