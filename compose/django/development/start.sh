#!/bin/sh
python manage.py makemigrations
python manage.py migrate
/usr/local/bin/gunicorn config.wsgi:application -w 2