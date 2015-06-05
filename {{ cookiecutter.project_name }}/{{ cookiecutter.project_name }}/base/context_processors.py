from django.conf import settings as django_settings


def settings(request):
    """
    Adds static-related context variables to the context.

    """
    return {'settings': django_settings}
