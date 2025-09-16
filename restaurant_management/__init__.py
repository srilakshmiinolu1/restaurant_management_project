from django.db import models
from products.models import Product
class OrderStatus(mmodel.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
class Order(models.Model):
    customer_name = models.CharField(max_length=100)        
    order_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(Product, related_name="orders")
    coupon_code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"  