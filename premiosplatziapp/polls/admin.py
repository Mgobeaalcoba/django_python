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
    # Modificamos la vista de los distintos objetos del modelo en el Admin: 
    list_display = (
        "question_text",
        "pub_date",
        "was_published_recently",
    )
    # En este caso le digo que quiero ver los dos atributos y también el resultado de aplicar el metodo was...
    # También puedo aplicar filtros a mi Admin
    list_filter = [
        "pub_date"
    ]
    # Coloco un cuadro de busqueda para buscar por texto:
    search_fields = [
        "question_text"
    ]

admin.site.register(Question, QuestionAdmin)
