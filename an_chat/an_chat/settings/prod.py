from .base import *
import os
from pathlib import Path
from dotenv import load_dotenv

DEBUG = False

env_path = Path(".") / ".env"
load_dotenv(env_path)

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS_PROD").split(",")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("PG_DATABASE"),
        "USER": os.getenv("PG_USER"),
        "PASSWORD": os.getenv("PG_PASSWORD"),
        "HOST": "",  # Unix Socket is used
        "PORT": "",  # Unix Socket is used
        "OPTIONS": {
            "unix_socket": os.getenv("PG_UNIX_SOCKET"),  # Path to Unix Socket
        },
    }
}
