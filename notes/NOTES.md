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

