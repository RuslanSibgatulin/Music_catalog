
import os
from pathlib import Path

from split_settings.tools import include

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT", 5432),
        "OPTIONS": {
            "options": "-c search_path=public,content"
        }
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
STATIC_ROOT = "static"  # dir for collectstatic command

include(
    "components/logger.py",
    "components/middleware.py",
    "components/templates.py",
    "components/auth.py",
    "components/apps.py",
    "components/rest.py",
)
