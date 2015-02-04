#!/usr/bin/env python
"""Script for regenerating a test project from the sugardough template.

Usage:
  regenerate.py [--watch]
  regenerate.py (-h | --help)

Options:
  -h --help  Show this screen.
  --watch    Watch template directory for changes and regenerate
             automatically.

"""
from __future__ import print_function

import contextlib
import os
import time

from cookiecutter.main import cookiecutter
from docopt import docopt
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTDIR = os.path.join(BASEDIR, 'test_project')
DOUGHDIR = os.path.join(TESTDIR, 'sugardough')
TEMPLATEDIR = os.path.join(BASEDIR, '{{ cookiecutter.project_name }}')


@contextlib.contextmanager
def working_directory(path):
    """
    A context manager which changes the working directory to the given
    path, and then changes it back to its previous value on exit.

    Original by Greg Warner:
    http://code.activestate.com/recipes/576620-changedirectory-context-manager/#c3
    """
    prev_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)


def regenerate():
    with working_directory(TESTDIR):
        print('Regenerating test directory...', end='')
        cookiecutter(BASEDIR, no_input=True)
        print('Done')


class RegenerateSugardoughHandler(PatternMatchingEventHandler):
    """
    Regenerate the sugardough test project whenever anything changes.
    """
    def on_any_event(self, event):
        regenerate()


def main(watch):
    # Regenerate at least once.
    regenerate()

    if watch:
        observer = Observer()

        # Observe both the template directory and cookiecutter.json.
        observer.schedule(RegenerateSugardoughHandler(), TEMPLATEDIR, recursive=True)
        cookiecutter_json_handler = RegenerateSugardoughHandler(patterns=[
            os.path.join(BASEDIR, 'cookiecutter.json')
        ])
        observer.schedule(cookiecutter_json_handler, BASEDIR)

        print('Watching for changes...')
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()


if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(watch=arguments['--watch'])
