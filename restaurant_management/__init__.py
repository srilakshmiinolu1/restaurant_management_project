from django.db import models
from django.contrib.auth.models import User
class Order(models.Model):
    user = models.Foreignkey(User, on_delete=models.CASCADE, related_name="orders")
    date = models.DataTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
        class OrderItem(models.Model):
            oder = models.Foreignkey(order, on_delete=models.CASCADE, related_name="items")
            product_name = models.CharField(max_length=100)
            quantity = models.PositiveIntegerField()
            price = models.DecimalField(max_digits=10, decimal_places=2)
            def __str__(self):
                return f"{self.product_name} (x{self.quantity})"