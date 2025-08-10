from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    # Keep a short, stable label so existing migrations remain valid
    label = 'api'
