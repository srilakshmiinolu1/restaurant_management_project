from django.db import models
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    opening_days = models.CharFiled(max_length=100, max_length="Enter days like: Mon,Tue,Wed,Thu,Fri,Sat,Sun ")       
    def __str__(self):
        return self.name
         