from django.db import models
class OrderStatus(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Order(models.Model):
    customer_name = models.CharFields(max_length=100)
    order_data = models.DataTimeField(auto_now_add=True)
    amount = models.DecimalFiled(max_digits=10, decimal_places=2)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL,
    null=Tree,
    blank=True
    )
    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"        


    
