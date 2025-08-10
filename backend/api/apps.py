from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Full dotted path to the app package:
    name = 'backend.api'
    # Keep the short label so existing migrations/table names don't change:
    label = 'api'
