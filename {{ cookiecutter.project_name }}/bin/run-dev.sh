#!/bin/sh

urlwait  # Wait for the database to come online
./bin/run-common.sh
./manage.py runserver 0.0.0.0:8000
