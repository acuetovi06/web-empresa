from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
    verbose_name = 'Gestor de Servicios'  # This is the name that will be used in the Django admin interface and other places where the app name is displayed.
