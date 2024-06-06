import django.db import models

customer1 = Customer(models.Model):
    name = models.CharField(max_length=100)