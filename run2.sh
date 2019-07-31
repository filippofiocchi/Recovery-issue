#!/bin/sh
cd /home/pi/recovery-issue
PATH=/usr/local/bin:$PATH
export TOKEN_GITHUB='your github token'
export TOKEN_BITLY='your bitlytoken'
export NAME_ORGANIZZATION='the name of the organizzation on github'
export FLASK_APP=flask_recovery.py
/usr/local/bin/pipenv run flask run --host=0.0.0.0
