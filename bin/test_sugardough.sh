#!/bin/bash
set -e

TDIR=`mktemp -d`
cp cookiecutter.json $TDIR/
cd $TDIR
cookiecutter --no-input $OLDPWD
cd sugardough
tox -e $TOX_ENV
