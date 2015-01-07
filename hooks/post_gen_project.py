#!/usr/bin/env python

from uuid import uuid4

print('Generating development .env file')

variables = {
    'DEBUG': 'True',
    'ALLOWED_HOSTS': 'localhost, 127.0.0.1',
    'SECRET_KEY': str(uuid4()),
    }

with open('.env', 'w') as environment:
    for key, value in variables.items():
        environment.write('{key}={value}\n'.format(key=key, value=value))
