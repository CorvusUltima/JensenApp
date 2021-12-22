from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProfilePages'


    def ready(self):
        import ProfilePages.signals