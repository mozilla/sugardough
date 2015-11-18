Sugardough
==========

Sugardough is a web application template based on Django. Sugardough is
build using [Cookiecutter](https://github.com/audreyr/cookiecutter).

Features:
 * Django settings with environment variables, using [Decouple](https://github.com/henriquebastos/python-decouple)
 * [Jinja2](http://jinja.pocoo.org/) template engine
 * [Whitenoise](http://whitenoise.evans.io/)
 * [Docker](https://docker.io/) ready, plus [Docker Compose](https://github.com/docker/compose) support.
 * Sane [Flake8](http://flake8.readthedocs.org/en/2.2.3/) configuration.
 * [NewRelic](https://newrelic.com/) ready.
 * [Travis-CI](http://travis-ci.org/) ready.
 * [Coveralls](http://coveralls.io/) ready.
 * [Sphinx](http://sphinx-doc.org/) support and [ReadTheDocs](https://readthedocs.org/) ready.
 * [peep](https://github.com/erikrose/peep) ready.
 * [session-csrf](https://github.com/mozilla/django-session-csrf) included.

[![Requirements Status](https://img.shields.io/requires/github/mozilla/sugardough.svg)](https://requires.io/github/mozilla/sugardough/requirements/?branch=master)

Virtualenv
[![Build Status](https://img.shields.io/travis/mozilla/sugardough/master.svg)](https://travis-ci.org/mozilla/sugardough)
Docker
[![Build Status](https://ci.us-west.moz.works/buildStatus/icon?job=sugardough)](https://ci.us-west.moz.works/job/sugardough)



Create a sugardough project
---------------------------

1. Get cookiecutter:

   ```sh
   $ pip install cookiecutter
   ```
2. Run cookiecutter with sugardough template

   ```sh
   $ cookiecutter https://github.com/mozilla/sugardough
   ```
3. Done!


Contribute to sugardough
------------------------

To contribute to sugardough development:

1. Clone this repository
2. Create a [virtualenv](https://virtualenv.pypa.io/en/latest/).
3. Install development requirements using pip:

   ```sh
   $ pip install -r requirements.txt
   ```
4. Update the [template directory], and [cookiecutter.json] as well with new
   variables if needed.
5. Run the regeneration script that auto-creates a test site:

   ```sh
   $ ./bin/regenerate.py
   ```
6. Launch the test site to see your changes:

   ```sh
   $ cd test_project/sugardough
   $ docker-compose up
   ```
6. Git commit changes.
7. Pull request!

 [template directory]: https://github.com/mozilla/sugardough/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D
 [cookiecutter.json]: https://github.com/mozilla/sugardough/blob/master/cookiecutter.json

The `regenerate.py` command can also watch for changes and auto-regenerate the
test project:

```sh
$ ./bin/regenerate.py --watch
```

If you want the test project to use a different value for a variable than the
default defined in `cookiecutter.json`, add the value to your
`~/.cookiecutterrc` file:

```
default_context:
    project_name: "Foo Bar"
```


Opinions
--------

* If you want to change the rules for **PEP8**, go and edit the `setup.cfg` file.

* If you want to use **MySQL** instead of PostgreSQL (which is default),
edit the generated `requirements.txt` file and remove the lines about
`psycopg2` then use `peep` to add the version of `MySQL-python` you want to
use. You will also need to edit the `.travis.yml` file accordingly.

* if you want to use **pytest**  add in requirements.txt `pytest`, `py`,
`cov-core` and `pytest-django`.
For test coverage you'll also have to add `pytest-cov`.
Next you'll need to edit the `.travis.yml` file and edit the script part.
Instead of `coverage run manage.py test` it
`py.test --cov=sugardough`.

* Dockerfile uses Python 3. If you want Python 2 change line 'FROM python:3-slim'
 to 'FROM python:2-slim'


License
-------

Sugardough itself is licensed under the [Apache 2 license](http://www.apache.org/licenses/LICENSE-2.0). See the [LICENSE](LICENSE) file in this repository for the full text of the license. The website projects produced using sugardough use the [Mozilla Public License version 2](https://www.mozilla.org/MPL/2.0/) by default.
