from django.apps import AppConfig

import session_csrf


class BaseAppConfig(AppConfig):
    name = '{{ cookiecutter.project_name }}.base'

    def ready(self):
        # The app is now ready. Include any monkey patches here.

        # Monkey patch CSRF to switch to session based CSRF. Session
        # based CSRF will prevent attacks from apps under the same
        # domain. If you're planning to host your app under it's own
        # domain you can remove session_csrf and use Django's CSRF
        # library. See also
        # https://github.com/mozilla/sugardough/issues/38
        session_csrf.monkeypatch()
