from django.contrib.staticfiles.templatetags.staticfiles import static
from jingo import register


static = register.function(static)
