from django.db import models
from django.conf import settings
from home.models import Product
class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order{self.order_id} by {self.customer}"
class OrderItem(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


