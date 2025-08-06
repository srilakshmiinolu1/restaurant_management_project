from rest_framework import models
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_degits=6, decimal_places=2)
    def __str__(self):
        return self.name


    
