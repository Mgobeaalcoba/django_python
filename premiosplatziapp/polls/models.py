from django.db import models

# Create your models here.

# Django transformara nuestras clases a tablas en nuestra base de datos sqlite3
class Question(models.Model):
    # Definimos los atributos de esta clase que se corresponden con las columnas de la tabla Question: 
    # id no es necesario dado que Django lo genera solo de forma autoincremental
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(name="date published")

# Segundo modelo Choices
class Choices(models.Model):
    # id
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Llave foranea que establece la relación 1 - muchos entre mis models
    # El on_delete=models.CASCADE establece que si se borra una Question se deben borrar todas las choices de esa question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
