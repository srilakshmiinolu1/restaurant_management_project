from django.apps import AppConfig
class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    def ready(self):
        from .models import OrderStatus
        default_statuses = ["pending", "Processing", "Completed", "Cancelled"]
        for status in default_statuses:
            OrderStatus.objects.get_or_create(name=status)
            