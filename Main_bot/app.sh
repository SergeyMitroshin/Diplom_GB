#!/usr/bin/env bash
BASEDIR=$(dirname "$0")
echo "Executing App in '$BASEDIR'"
PORT=$1
source $BASEDIR/env/bin/activate
python $BASEDIR/app.py $PORT
