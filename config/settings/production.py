from .default import *


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': 'postgres',
        'PORT': 5432,
    }
}

# Use Whitenoise to serve static files
# ------------------------------------------------------------------------------
# https://whitenoise.readthedocs.io/

MIDDLEWARE = DJANGO_SECURITY_MIDDLEWARE
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware'] + DJANGO_MIDDLEWARE
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Use Gunicorn as WSGI HTTP server
# ------------------------------------------------------------------------------
# http://gunicorn.org/

INSTALLED_APPS += ['gunicorn']


# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts

# ALLOWED_HOSTS = config(
#     'ALLOWED_HOSTS',
#     cast=lambda v: [d for d in [s.strip() for s in v.split(' ')] if d],
#     default='')


# EMAIL CONFIGURATION - Anymail with Mailgun
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/topics/email/
# https://github.com/anymail/django-anymail

# INSTALLED_APPS += ('anymail')
# ANYMAIL = {'MAILGUN_API_KEY': config('MAILGUN_API_KEY')}


# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                '%(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'},
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'mail_admins'],
            'propagate': True
        }
    }
}
