from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return self.name

class Order(models.Model):
      price = models.DecimalField(max_digits=7, decimal_places=2)
      order_date = models.DateField(auto_now=True)
      customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    
