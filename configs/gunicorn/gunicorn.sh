#!/bin/bash
set -e

NAME="VistaTurbine Gunicorn"
VistaTurbine_ENV_NAME="venv"
VistaTurbine_PATH=/VistaTurbine
DJANGO_WSGI_MODULE=VistaTurbine.wsgi

echo "Starting $NAME as `whoami`"

cd $VistaTurbine_PATH

exec supervisord
exec gunicorn -c $VistaTurbine_PATH/configs/gunicorn/gunicorn.conf.py ${DJANGO_WSGI_MODULE}