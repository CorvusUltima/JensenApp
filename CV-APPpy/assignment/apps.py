from django.apps import AppConfig


class assignmentConfig(AppConfig):
    name = 'assignment'

    def ready(self):
        import assignment.signals
