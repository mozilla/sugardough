Sugardough
==========

Sugardough is a web application template based on Django. Sugardough is
build using [Cookiecutter](https://github.com/audreyr/cookiecutter).

Features:
 * Django settings with environment variables, using [Decouple](https://github.com/henriquebastos/python-decouple)
 * [Jinja2](http://jinja.pocoo.org/) template engine with [Jingo](http://jingo.readthedocs.org/)
 * [Whitenoise](http://whitenoise.evans.io/)
 * [Docker](https://docker.io/) ready, plus [Fig](http://fig.sh/) support.
 * Sane [Flake8](http://flake8.readthedocs.org/en/2.2.3/) configuration.
 * [NewRelic](https://newrelic.com/) ready.
 * [Travis-CI](http://travis-ci.org/) ready.
 * [Coveralls](http://coveralls.io/) ready.
 * [Sphinx](http://sphinx-doc.org/) support and [ReadTheDocs](https://readthedocs.org/) ready.
 * [peep](https://github.com/erikrose/peep) ready.

[![Requirements Status](https://requires.io/github/mozilla/sugardough/requirements.svg?branch=master)](https://requires.io/github/glogiotatidis/sugardough/requirements/?branch=master)

Create a sugardough project
---------------------------

1. Get cookiecutter:

    $ pip install cookiecutter

2. Run cookiecutter with sugardough template

    $ cookiecutter https://github.com/mozilla/sugardough

3. Done!


Cooking sugardough
------------------

To contribute to sugardough development:

 1. Clone this repository
 2. Make your changes in [sugardough](https://github.com/mozilla/sugardough/tree/master/sugardough) directory
 3. Update [cookiecutter.json](https://github.com/mozilla/sugardough/blob/master/cookiecutter.json) with new variables if needed.
 4. Delete existing template directory:
    $ rm -rf "{{ cookiecutter.project_name }}"
 5. Run ./bin/fabricate-cookiecutter.py
 6. Git commit changes. Note both "sugardough" and "{{ cookiecutter.project_name }}" directories must be committed.
 7. Pull request!

Alternativelly you can use the pre-commit git hook to do steps 4 and 5 automagically every time you commit. Just link `./git-hooks/post-commit` to `./.git/hooks/post-commit`:

 `$ ln -s ../../git-hooks/post-commit .git/hooks/post-commit`
