from django.db import models
from django.contrib.auth.models import User
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_names = "orders")
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
        class OrderItem(models.Model):
            order = models.ForeignKey(order, on_delete=models.CASCADE, related_names = "items")
            product_name = models.CharField(max_length=100)
            quantity = models.PositiveIntegerField()
            price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.product_name} (x{self.quantity})"