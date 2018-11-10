#!/bin/bash
set -e

NAME="SDP Gunicorn"
SDP_ENV_NAME="SDP_env"
SDP_PATH=/SDP
DJANGO_WSGI_MODULE=SDP.wsgi

echo "Starting $NAME as `whoami`"

cd $SDP_PATH

exec supervisord
exec gunicorn -c $SDP_PATH/configs/gunicorn/gunicorn.conf.py ${DJANGO_WSGI_MODULE}