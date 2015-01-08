import sys

import decouple


try:
    from .base import *  # noqa
except decouple.UndefinedValueError as exp:
    print('ERROR:', exp.message)
    sys.exit(1)
