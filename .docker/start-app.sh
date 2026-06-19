#!/bin/sh
set -e

APP_HOST="${APP_HOST:-0.0.0.0}"
APP_PORT="${APP_PORT:-8000}"
DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE:-config.settings}"
DJANGO_RUNSERVER="${DJANGO_RUNSERVER:-false}"
GUNICORN_WORKERS="${GUNICORN_WORKERS:-2}"

export DJANGO_SETTINGS_MODULE

if [ "$DJANGO_RUNSERVER" = "true" ]; then
    exec python manage.py runserver "$APP_HOST:$APP_PORT"
fi

exec gunicorn config.wsgi:application \
    --bind "$APP_HOST:$APP_PORT" \
    --workers "$GUNICORN_WORKERS"
