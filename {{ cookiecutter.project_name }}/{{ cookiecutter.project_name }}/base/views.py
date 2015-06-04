from django.shortcuts import render


def home(request):
    return render(request, '{{ cookiecutter.project_name }}/home.html')
