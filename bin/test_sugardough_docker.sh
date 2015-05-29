#!/bin/bash
set -e

TDIR=`mktemp -d`
virtualenv $TDIR
. $TDIR/bin/activate
pip install tox cookiecutter
TOX_ENV=dockertests ./bin/test_sugardough.sh
