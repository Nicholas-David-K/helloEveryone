from django.apps import AppConfig


class TaifaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'taifa'

    def ready(self):
        import taifa.signals