from .base import *
from .base import env

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
