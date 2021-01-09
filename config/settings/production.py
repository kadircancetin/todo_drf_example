from config.settings.base import *  # NOQA

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "production_db.sqlite3"),  # noqa
    }
}
