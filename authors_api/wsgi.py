import os

from django.core.wsgi import get_wsgi_application

# -Define local by default
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.local")

application = get_wsgi_application()
