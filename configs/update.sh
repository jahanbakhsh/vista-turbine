#!/bin/bash
set -e

DORSA_PATH=/dorsa
DJANGO_REQUIREMENT_PATH=requirements/development.txt
VIRTUAL_ENV_ACTIVE_PATH=~/.virtualenvs/dorsa/bin/activate
NAME="DORSA Init"

echo "Starting $NAME as `whoami`"


. $VIRTUAL_ENV_ACTIVE_PATH
cd $DORSA_PATH/requirements
pip install -U -r production.txt



