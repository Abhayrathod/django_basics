from django.apps import AppConfig


class OnetooneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'onetoOne'
    def ready(self):
        import onetoOne.signals