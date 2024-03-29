import socket
from .default import *  # noqa


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),  # noqa
    }
}

# Django Debug Toolbar
# ------------------------------------------------------------------------------
# https://github.com/jazzband/django-debug-toolbar

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INSTALLED_APPS += ['debug_toolbar']
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']

# Hack to have debug toolbar when developing with docker
ip = socket.gethostbyname(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + "1"]

SITE_ID = 1
