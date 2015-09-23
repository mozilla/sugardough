from django.shortcuts import render

from session_csrf import anonymous_csrf


@anonymous_csrf
def home(request):
    return render(request, '{{ cookiecutter.project_name }}/home.jinja')
