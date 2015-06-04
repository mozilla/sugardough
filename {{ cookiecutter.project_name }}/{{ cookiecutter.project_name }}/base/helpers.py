import datetime
import urllib
import urlparse

import jinja2
from django.conf import settings as django_settings
from django.utils.encoding import smart_str


def settings(request):
    """
    Adds static-related context variables to the context.

    """
    return {'settings': django_settings}


def thisyear():
    """The current year."""
    return jinja2.Markup(datetime.date.today().year)


def urlparams(url_, hash=None, **query):
    """Add a fragment and/or query paramaters to a URL.
    New query params will be appended to exising parameters, except duplicate
    names, which will be replaced.
    """
    url = urlparse.urlparse(url_)
    fragment = hash if hash is not None else url.fragment

    # Use dict(parse_qsl) so we don't get lists of values.
    q = url.query
    query_dict = dict(urlparse.parse_qsl(smart_str(q))) if q else {}
    query_dict.update((k, v) for k, v in query.items())

    query_string = _urlencode([(k, v) for k, v in query_dict.items()
                               if v is not None])
    new = urlparse.ParseResult(url.scheme, url.netloc, url.path, url.params,
                               query_string, fragment)
    return new.geturl()


def _urlencode(items):
    """A Unicode-safe URLencoder."""
    try:
        return urllib.urlencode(items)
    except UnicodeEncodeError:
        return urllib.urlencode([(k, smart_str(v)) for k, v in items])
