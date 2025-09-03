"""
ASGI config for django_website_bgx project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/

asgi => point d’entrée pour déploiement asynchrone (WebSocket, etc.).
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_website_bgx.settings")

application = get_asgi_application()
