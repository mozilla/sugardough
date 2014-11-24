#!/usr/bin/env python
import fileinput
import shutil
import os
import json
import subprocess

BASEDIR = os.path.dirname(os.path.dirname(__file__))
DOUGHDIR = os.path.join(BASEDIR, 'sugardough')
DOUGHDIR_TEMP = os.path.join(BASEDIR, 'sugardough-temp')


def global_replace(FROM, TO, dry_run=False):
    for dirpath, dirnames, filenames in os.walk(DOUGHDIR_TEMP, topdown=False):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            new_filename = filename.replace(FROM, TO)
            new_full_path = os.path.join(dirpath, new_filename)
            shutil.move(full_path, new_full_path)

        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            new_dirname = dirname.replace(FROM, TO)
            new_full_path = os.path.join(dirpath, new_dirname)
            shutil.move(full_path, new_full_path)

    files = []
    for dirpath, dirnames, filenames in os.walk(DOUGHDIR_TEMP, topdown=False):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))

    fi = fileinput.input(files, inplace=1)
    for lines in fi:
        print lines.replace(FROM, TO),

subprocess.call(
    'git archive --format=tar --prefix=sugardough-temp/ HEAD:sugardough | tar xf -',
    shell=True
)

with open(os.path.join(BASEDIR, 'cookiecutter.json')) as fp:
    cookiecutter = json.load(fp)

for key, value in sorted(cookiecutter.items(), key=lambda x: len(x[1]), reverse=True):
    global_replace(value, '{{ cookiecutter.%s }}' % key)

new_dirname = os.path.basename(DOUGHDIR_TEMP).replace('-temp', '')
new_dirname = new_dirname.replace('sugardough', '{{ cookiecutter.project_name }}')
new_full_path = os.path.join(BASEDIR, new_dirname)
shutil.move(DOUGHDIR_TEMP, new_full_path)


