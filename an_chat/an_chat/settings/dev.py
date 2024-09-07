from .base import *
import os
from pathlib import Path
from dotenv import load_dotenv

DEBUG = True

env_path = Path(".") / ".env"
load_dotenv(env_path)

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS_DEV").split(",")

INSTALLED_APPS += [
    "django_extensions",
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("PG_DATABASE"),
        "USER": os.getenv("PG_USER"),
        "PASSWORD": os.getenv("PG_PASSWORD"),
        "HOST": os.getenv("PG_HOST"),
        "PORT": os.getenv("PG_PORT"),
    }
}
