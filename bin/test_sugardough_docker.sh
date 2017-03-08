#!/bin/bash
#
# Runs unit_tests
#
set -ex
# Create a temporary virtualenv to install docker-compose
ENVDIR=`mktemp -d`
virtualenv $ENVDIR
. $ENVDIR/bin/activate
pip install cookiecutter docker-compose

TDIR=`mktemp -d`
cp cookiecutter.json $TDIR/
cd $TDIR
cookiecutter --no-input $OLDPWD
cd sugardough

docker-compose run -T web flake8 sugardough
docker-compose run -T web bash -c 'urlwait && ./manage.py test'

# Delete virtualenv
rm -rf $TDIR $ENVDIR
