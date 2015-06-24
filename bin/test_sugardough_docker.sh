#!/bin/bash
#
# Runs unit_tests
#
set -ex
# Create a temporary virtualenv to install docker-compose
ENVDIR=`mktemp -d`
virtualenv $ENVDIR
. $ENVDIR/bin/activate
pip install cookiecutter docker-compose==1.2.0

TDIR=`mktemp -d`
cp cookiecutter.json $TDIR/
cd $TDIR
cookiecutter --no-input $OLDPWD
cd sugardough

DC_CMD="docker-compose --project-name jenkins${JOB_NAME}${BUILD_NUMBER}"

$DC_CMD run -T web flake8 sugardough

# Run Tests
$DC_CMD run -T web ./manage.py test

# Delete virtualenv
rm -rf $TDIR $ENVDIR
