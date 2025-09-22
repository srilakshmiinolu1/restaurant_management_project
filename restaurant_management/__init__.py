from django.db import models
class ActiveOrderManger(models.Manager):
    daf active_orders(slef):
    return
super().get_queryset().filter(status__in=['pending','processing'])
class Order(models.Model):
    STATUS_CHOICES = [('pending','Pending'),('processing','Processing'),('completed','Completed'),('cancelled','Cancelled'),]
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DataTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.id} - {self.customer_name} ({self.status})"    