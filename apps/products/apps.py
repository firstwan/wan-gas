from django.apps import AppConfig

# Configuration of this module
class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'
    label = 'products'

    def ready(self):
        from . import signals