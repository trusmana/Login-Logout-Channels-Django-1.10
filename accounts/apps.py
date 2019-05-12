from django.apps import AppConfig

class CekLogin(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
