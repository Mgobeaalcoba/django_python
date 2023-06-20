import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# Django transformara nuestras clases a tablas en nuestra base de datos sqlite3
class Question(models.Model):
    # Definimos los atributos de esta clase que se corresponden con las columnas de la tabla Question: 
    # id no es necesario dado que Django lo genera solo de forma autoincremental
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(name="pub_date")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now()  - datetime.timedelta(days=1) and self.pub_date <= timezone.now()

# Segundo modelo Choices
class Choice(models.Model):
    # id
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Llave foranea que establece la relación 1 - muchos entre mis models
    # El on_delete=models.CASCADE establece que si se borra una Question se deben borrar todas las choices de esa question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

## Cada vez que haga un cambio en los modelos tengo que ejecutar los dos comandos para activar y trabajar con el ORM
