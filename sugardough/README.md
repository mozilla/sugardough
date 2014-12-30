sugardough
==========

[![Build Status](https://img.shields.io/travis/mozilla/sugardough/master.svg)](https://travis-ci.org/mozilla/sugardough)

[![Coverage status](https://img.shields.io/coveralls/mozilla/sugardough/master.svg)](https://coveralls.io/r/mozilla/sugardough)

Run the tests
-------------

There's a sample test in `sugardough/base/tests.py` for your convenience, that
you can run using the following command:

    python manage.py test

If you want to run the full suite, with flake8 and coverage, you may use
[tox](https://testrun.org/tox/latest/). This will run the tests the same way
they are run by [travis](https://travis-ci.org)):

    pip install tox
    tox

The `.travis.yml` file will also run [coveralls](https://coveralls.io) by
default.

If you want to benefit from Travis and Coveralls, you will need to activate
them both for your project.

Oh, and you might want to change the "Build Status" and "Coverage Status" links
at the top of this file to point to your own travis and coveralls accounts.


Docker for development
----------------------

0. Make sure you have [docker](https://docker.io) and [fig](https://pypi.python.org/pypi/fig)
1. fig up


Docker for deploying to production
-----------------------------------

1. Add your project in [Docker Registry](https://registry.hub.docker.com/) as [Automated Build](http://docs.docker.com/docker-hub/builds/)
2. Prepare a 'env' file with all the variables needed by dev, stage or production.
3. Run the image:

    docker run --env-file env -p 80:80 mozilla/sugardough


NewRelic Monitoring
-------------------

A newrelic.ini file is already included. To enable NewRelic monitoring
add two enviroment variables:

 - NEW_RELIC_LICENSE_KEY
 - NEW_RELIC_APP_NAME

See the [full list of supported environment variables](https://docs.newrelic.com/docs/agents/python-agent/installation-configuration/python-agent-configuration#environment-variables).
