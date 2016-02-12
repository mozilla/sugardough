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

PROJECT_NAME=`echo "jenkins${JOB_NAME}${BUILD_NUMBER}" | sed s/_//g`
DC_CMD="docker-compose --project-name $PROJECT_NAME"

$DC_CMD run -T web flake8 sugardough

# Wait for database
$DC_CMD up -d db
while true;
do
    CMD="docker run --link ${PROJECT_NAME}_db_1:db multicloud/netcat -z db 5432"
    if eval ${CMD};
    then
        break;
    fi;
    sleep 1s;
done;

# Run Tests
$DC_CMD run -T web ./manage.py test

# Delete virtualenv
rm -rf $TDIR $ENVDIR
