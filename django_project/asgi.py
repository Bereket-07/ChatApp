"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter
from chat import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
application = ProtocolTypeRouter({
    "http" : get_asgi_application() , 
    "websocket" : AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )    
        )
})

ASGI_APPLICATION = 'django_project.asgi.application'
