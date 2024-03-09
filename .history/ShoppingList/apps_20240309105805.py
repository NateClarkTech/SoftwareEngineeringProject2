from django.apps import AppConfig

class ShoppinglistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ShoppingList'

    def ready(self):
        import ShoppingList.signals