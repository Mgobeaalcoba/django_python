"""
ASGI config for premiosplatziapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# Archivo de django que nos permite hacer el deploy de una aplicación

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'premiosplatziapp.settings')

application = get_asgi_application()
