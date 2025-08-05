from django.db import models
from django.contrib.auth.models import User
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_items_description = models.TextField(help_text="Description of items in the order")
    total_amount = models.DecimalField(max_text=10, decimal_places=2)
    ORDER_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    created_at = models.DataTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
    def __str__(self):
        return f"Order {self.id} - {self.customer.username}"
