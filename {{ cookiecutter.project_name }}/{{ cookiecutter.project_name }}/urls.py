from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from {{ cookiecutter.project_name }}.base import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),

    # contribute.json url
    url(r'^(?P<path>contribute\.json)$', 'django.views.static.serve',
        {'document_root': settings.ROOT}),
]
