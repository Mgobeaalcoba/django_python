# Django-Python

## ¿Qué es Django?

**Django** es uno de los framework gratis y open source más populares para crear aplicaciones web. Es muy veloz, seguro y escalable.
Es el segundo framework de desarrollo web más usado, siendo **Flask** el más usado solo por un 1% y el tercero siendo **FastAPI**.

Ranking de framework python para desarrollo web: 

<img src="../images/ranking_frameworks.PNG">

Algunos proyectos que usan Django son:

- Instagram
- Pinterest
- National Geographic
- Platzi

------------------------------------------------

## ¿¿¿Flask, Django o FastApi???

Si existe un lenguaje más que versátil para construir el motor de tu siguiente aplicación, ese es Python.

El backend es la sección de una aplicación móvil o web, donde sucede la **lógica de negocio**. Y la lógica de negocio, no es nada más ni nada menos que **la resolución del problema que intenta abordar esa aplicación.**

Para lograr este heroico cometido, se crearon los famosos y tan populares frameworks de desarrollo web. Hay decenas. Seguramente me equivoco, deben haber cientos de ellos. Uno para cada lenguaje, para cada gusto, para cada personalidad o estilo de trabajo incluso.

Aquí no vinimos a verlos a todos, solo a los más importantes, y en Python, solo tres ocupan este podio: Django, Flask y FastAPI.

Con los tres se pueden crear las mismas cosas. Son igual de válidos. Pero sí es cierto que cada uno tiene sus puntos fuertes, como también sus puntos débiles. Conozcamoslos uno a uno.

- El tanque: Django

Django es un framework robusto y cargado. Esas dos palabras lo definen perfectamente. Con una documentación de más de 3000 páginas te llevará de la mano a crear la aplicación web de tus sueños.

¿Qué lo hace sumamente especial y diferente al resto? Tiene el mejor sistema de control y manejo de datos que puedas encontrar en el ecosistema de Python.

Cuenta con un administrador ya programado de base extremadamente potente. Serás capaz de realizar las tareas más comunes en tu base de datos, como crear, borrar, actualizar y leer registros de tus tablas. Y esto se traduce, en la práctica, en poder dar de alta a un usuario y modificar su información rápidamente, si es que tu aplicación posee un sistema de login. O, también, por ejemplo, eliminar rápidamente una película de tu plataforma por errores en la subida, si es que estás construyendo el próximo Netflix.

Django cuenta con un 45% de acogida entre todos los desarrolladores web que trabajan con el lenguaje de la serpiente.
Y, con compañías como Instagram y Platzi usándolo todos los días, es una gran elección para comenzar.

- El heroe: Flask

5 años más jóven que Django, y nacido para destronar al rey. ¿Tienes una idea en mente, pero no quieres pasar por todo el proceso de configuración y establecimiento del entorno que tiene Django? Flask es tu elección. ¿Te interesa usar una base de datos no relacional en tu app? Django te lo permite… pero permíteme desaconsejarte hacer eso. ¿Por qué? Porque Flask permite realizar una conexión mucho más sencilla y con menos pasos a estos novedosos almacenes de datos.

Con un 46% de uso entre todos los desarrolladores web con Python, y con empresas como Netflix y Reddit apoyándose en este proyecto durante cada jornada para hacer vivir sus aplicaciones, es también una gran decisión empezar por Flask.

- La jóven promesa: FastAPI

Con solo tres años de edad, al día de publicación de este blogspot, FastAPI promete convertirse en el framework definitivo para la nueva generación de aplicaciones web que ya están naciendo.

Veloz. Solo esa palabra lo define. Es (y no solo en Python, sino hablando en comparación a todos los otros lenguajes de programación) una de las herramientas más veloces para construir un backend, peleando mano a mano con bestias de la velocidad como Go o Node.js.

¿Quieres hacer menos de 10 líneas de código Python y tener un backend 100% funcional, corriendo en tu computadora? FastAPI. ¿Quieres crear tu primera API (Application Program Interface) para conectar todos los componentes de tu aplicación? FastAPI. Pero, sobre todo… ¿Te interesa que tu aplicación sea una de las más veloces del mercado, y que tus usuarios no paren de admirar los milisegundos que tarda en cargarse la primera página de tu proyecto? FastAPI.

Con un 14% de uso entre todos los desarrolladores web con Python, utilizado por Netflix, Uber, y empresas tan grandes como Microsoft, en Platzi hoy le apostamos a FastAPI.

Creemos fielmente que iniciar tu camino como cinturón negro en Python de la mano de este framework es la mejor ruta para convertirte en un profesional del desarrollo backend. 

-------------------------------------------------

## Instalación de Django

1. Con el entorno virtual creado y activo, nuestro repo activo y enlazado, el gitignore armado corremos: 

```bash
pip install django
```

2. Inicializo mi proyecto django con el siguiente comando: 

```bash
django-admin startproject premiosplatziapp
```
Este comando va a armar toda una estructura para nuestro proyecto con el nombre que le hemos asignado dentro de la carpeta donde estemos trabajando. 

---------------------------------------------

## Explorando los archivos que creó Django

- manage.py

Nos muestra a nosotros, owners del proyecto diferentes comandos que tenemos a disposición para hacer que el proyecto funcione. 

- premiosplatziapp/__init__.py

Archivo clasico de python que nos indica que una carpeta es un paquete

- premiosplatziapp/asgy.py & premiosplatziapp/wsgi.py

Archivo de django que nos permite hacer el deploy de una aplicación

Nos quedan los dos que son los mas importantes y que vamos a modificar mucho mientras estemos desarrollando el proyecto: 

- **premiosplatziapp/settings.py**

Contiene toda la información sobre la configuración de nuestro proyecto

- **premiosplatziapp/urls.py**

Contiene todas las URL por las que va a funcionar nuestro proyecto. 

--------------------------------------------

## El servidor de desarrollo

Cuando trabajamos desarrollando servidores web en backend contamos con dos servidores distintos. Uno local, que vive en localhost y sobre el cual trabajamos las ediciones y correciones necesarias y uno de producción que es el que vive en la web y sobre el cual no hacemos ediciones nunca. Si hay algo para corregir lo corregimos en local y luego volvemos a deployar el proyecto. 

Django nos permite trabajar con un servidor de desarrollo que nos facilita el trabajo y nos permite ver en tiempo real los cambios que hacemos en nuestro codigo. ¿Como lo usamos? 

1. Encendemos el servidor de desarrollo: 

```bash
python3 manage.py runserver
```
ó

```bash
py manage.py runserver
```

Nos dirigimos a http://127.0.0.1:8000/ y podremos ver nuestro servidor de desarrollo ya construido y funcionando aún sin contenido. Pero listo para que lo editemos. 

Al iniciar nuestro servidor Django va a crear una base de datos sqlite3 dentro del proyecto para poder almacenar allí los datos que correspondan. 

**IMPORTANTE**: La variable DEBUG en el archivo setting.py debe ser TRUE mientras estemos trabajando en modo desarrollo pero en cuanto llevemos nuestro proyecto a producción debemos asegurarnos antes que DEBUG pase a FALSE.

--------------------------------------

## Iniciando el proyecto Premios Platzi App

Algunas cosas que tenemos que saber antes de empezar en django: 

- Proyectos: conjuntos de aplicaciones. Instagram por ej es un proyecto formado por varias aplicaciones. 
- Aplicaciones. Ejemplo de aplicaciones de instagram: "feed", "stories", "messages", etc. 

Premios platzi app va a ser nuestro proyecto y dentro de ella vamos a construir distintas aplicaciones: "polls"

Trabajar con aplicaciones nos sirve para poder modularizar o componentizar nuestras aplicaciones, para poder trasladarlas de un proyecto a otro de forma muy simple. 

1. Dicho lo anterior, el comando inicial de django lo usamos para crear un proyecto pero ahroa debemos crear nuestra primer aplicación. La misma se debe crear dentro de la carpeta del proyecto que iniciamos anteriormente así: 

```bash
py manage.py startapp polls
```
Esto creo un paquete/carpeta "polls" dentro de la carpeta raiz de nuestro proyecto con una estructura de archivos que ya vamos a ir viendo en el transcurso de este proyecto. 

Ahora solo vamos a trabajar sobre el archivo views.py para crear un hola mundo. 

1. premiosplatziapp\premiosplatziapp\urls.py

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include("polls.urls")) # Importo todos los paths de la app "polls"
]
```

2. premiosplatziapp\polls\views.py

```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World")
```

3. Creo un archivo dentro del paquete "polls" llamado urls.py que voy a dejar así: 

```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```

-------------------------------------------

## Ajustando el archivo settings.py

- premiosplatziapp/premiosplatziapp/settings.py

1. **DATABASES**: 

```py
# Database. Acá podremos configurar con que base de datos vamos a trabajar. Por default Django trabaja con sqllite3
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Variantes: mysql, postgresql, oracle, etc. Todas relacionales.
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'USER'
        # 'PASSWORD'
    }
}
```

2. **TIME_ZONE**: 

```py
TIME_ZONE = 'America/Argentina/Buenos_Aires' # Definimos el timezone de nuestro proyecto. Para el caso de Arg sería UTC-3 pero se debe colocar con el codigo de timezone de arriba.

# De acá debemos sacar el timezone para el proyecto. Segunda columna: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
```

3. **INSTALLED_APPS**: Django ya cuenta con una serie de apps que por default le asigna a todos los proyectos: admin, auth, contenttypes, sessions, messages, staticfiles. A este deberíamos sumarle la app que ya creamos "polls"

```py
## Apps que trae Django por default.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

----------------------------------------

## ¿Que es ORM? ¿Que es un modelo? 

**ORM = Object Relational Mapping** nos explica como yo puedo relacionar, por un lado la estructura de una b**ase de datos relacional** (RDB) con, por el otro, la **programación orientada a objetos**

Ciertas librerías y frameworks me permiten replicar la estructura de una RBD con POO. Una de ellas es Django. 

En RDB cada entidad se corresponde en una tabla. 
En POO cada entidad se corresponde con un archivo.py

Ese archivo se va a llamar **model y se crea con clases de POO**

Cada tabla tiene columnas con atributos de mi entidad, pensemos en users: PK, username, password, fecha de creación, etc. Las columnas al trabajar con un ORM se corresponden con los atributos de nuestras clases. Cada una de las columnas también se define en RDB con un tipo de datos, al igual en nuestra clase también definiremos a cada uno de los atributos con un tipo de dato que son clases también a su vez. 

-------------------------------------------

## Creando un diagrama entidad-relación para nuestro proyecto

- app polls (dos tablas):

    - Questions (columnas/atributos): 
        - id: int (Primary Key - PK)
        - question_text: varchar
        - pub_date: datetime
    - Choices (columnas/atributos):
        - id: int (Primary Key - PK)
        - question: int (Llave foranea o foreign key -FK- que relaciona con el question id)
        - choice_text: varchar
        - votes: int

    Questions se relaciona con Choices de forma 1 a muchas.

----------------------------------------------

# Creando los modelos Question y Choice en codigo: 

Vamos a crear nuestras tablas diseñadas arriba en el diagram entidad-relación pero con el ORM de Django. 

1. Será en el archivo models.py de nuestra app polls donde trabajaremos todos lo relacionado a datos de nuestra aplicación. 

```py
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
```

2. Establezco en settings.py que la app que estamos construyendo es parte del proyecto así: 

```py
INSTALLED_APPS = [
    # Apps propias
    'polls.apps.PollsConfig',
    # Apps de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps de terceros si hubieses
]
```

3. Creo dentro de polls/migrations el archivo con la estructura que tiene que tener nuestra base de datos con el siguiente comando en la raiz del proyecto: 

```bash
21:41:23 👽 with 🤖 mgobea 🐶 in python/django_python/premiosplatziapp via django_python …
➜ python3 manage.py makemigrations polls
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choices
```
4. Ejecuto el ORM de Django para crear en mi base de datos sqlite3 mis tablas. Una por cada modelo. Esto lo hago con el siguiente comando también desde la raiz del proyecto: 

```bash
21:42:05 👽 with 🤖 mgobea 🐶 in python/django_python/premiosplatziapp via django_python …
➜ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying polls.0001_initial... OK
  Applying sessions.0001_initial... OK
```

Listo! Ya tenemos los modelos creados en models.py y también las bases de datos creadas en sqlite3!!!

-----------------------------------

## La consola interactiva de Django

Introducción: Python tiene una consola interactiva a la cual accedemos con python3 nuestra bash. 

- Consola Python: 

```py
21:52:25 👽 with 🤖 mgobea 🐶 in develop/python/django_python via django_python …
➜ python3
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hola mundo")
hola mundo
>>> numero_1 = 5
>>> numero_2 = 10
>>> numero_1 + numero_2
15
```

- Consola Django: nos posibilita interactuar con nuestros archivos. 

1. Para entrar correr en bash: 

```bash
python3 manage.py shell
```
Es importante que estés ubicado en la raiz de un proyecto Django para que funcione

2. Al abrir se va a ver casi igual que la consola de python, pero va a decir abajo entre parentesis (InteractiveConsole) que nos va a dar acceso al proyecto...

IMPORTANTE: Si modificamos el archivo models.py es necesario que volvamos a correr los dos comandos para que el ORM modifique nuestras tablas: 

```bash
python3 manage.py makemigrations polls

python3 manage.py migrate
```

Ahora si al entrar a la interactive console de Django vamos a poder importar las clases de nuestro modelo y usar el atributo objects.all() que nos permite traer todos los objetos que se crearon de nuestra clase: 

```bash
22:09:33 👽 with 🤖 mgobea 🐶 in python/django_python/premiosplatziapp via django_python …
➜ python3 manage.py shell
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from polls.models import Choice, Question
>>> Question.objects.all()
<QuerySet []>
>>> Choice.objects.all()
<QuerySet []>
>>>
```

En el ejemplo de arriba ⬆️ nos retorna un objeto QuerySet vacio dado que por el momento no hemos creado objetos de este tipo... 

Voy a importar de django.utils el modulo timezone para poder usar las clases de horarios con zonas horarias incorporadas y generar objetos dentro de mi consola interactiva de Django... 

```bash
22:25:57 👽 with 🤖 mgobea 🐶 in python/django_python/premiosplatziapp via django_python …
➜ python3 manage.py shell
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from polls.models import Choice, Question
>>> Question.objects.all()
<QuerySet []>
>>> Choice.objects.all()
<QuerySet []>
>>> from django.utils import timezone
>>> q = Question(question_text="¿Cual es el mejor curso de Platzi?", pub_date=ti
mezone.now())
>>> q.save()
```

En q guarde un objeto de tipo Question() y con q.save() estoy guardano ese objeto en mis bases de datos. 

---------------------------------------

## El metodo __str__

Cuando desde la consola interactiva de Django tenemos objetos creados y queremos conocerlos nos vamos a encontrar que al acceder al listado de objetos vamos a ver el nombre de los mismos pero no vamos a ver las descripciones. 

```bash
>>> q2 = Question(question_text="¿Cual es el mejor profesor de Platzi?", pub_dat
e=timezone.now())
>>> q2
<Question: Question object (None)>
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
>>> q2.save()
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>
>>> q2.question_text
'¿Cual es el mejor profesor de Platzi?'
>>> q2.pub_date
datetime.datetime(2023, 6, 18, 15, 45, 55, 663639, tzinfo=datetime.timezone.utc)
```

Como vemos el Question.objects.all() no es util para conocer todas nuestras preguntas. Para que lo sea tenemos que sumarle a nuestros modelos el metodo "dunderstring" o __str__ que permitirá retornar las preguntas, su texto en lugar del objeto completo. 

```py
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
        return self.pub_date >= timezone.now()  - datetime.timedelta(days=1)

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
```

Cuando los cambios en el modelo son sobre los metodos y no sobre los atributos no es necesario volver a correr el makemigrations polls y el migrate. 

Ahora al volver a abrir la consola interactiva de Django vamos a poder ver el contenido de nuestras preguntas al usar el metodo de nuestra clase heredada models .objects.all()

```bash
13:02:41 👽 with 🤖 mgobea 🐶 in python/django_python/premiosplatziapp via django_python took 20m 50.3s …
➜ python3 manage.py shell
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from polls.models import Question, Choice
>>> Question.objects.all()
<QuerySet [<Question: ¿Cual es el mejor curso de Platzi?>, <Question: ¿Cual es el mejor profesor de Platzi?>]>
>>>
```
----------------------------------

## Filtrando los objetos creados desde la consola interactiva:

Tenemos dos metodos especiales que nos brinda Django que nos permitiran hacer busquedas dentro de nuestras tablas. 
