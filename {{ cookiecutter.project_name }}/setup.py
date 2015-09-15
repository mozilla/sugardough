#!/usr/bin/env python

from distutils.core import setup

setup(
    name='{{ cookiecutter.project_name }}',
    version='0.1dev',
    description='This is https://github.com/mozilla/{{ cookiecutter.project_name }}',
    author='{{ cookiecutter.project_author }}',
    author_email='',
    url='https://github.com/mozilla/{{ cookiecutter.project_name }}'
)
