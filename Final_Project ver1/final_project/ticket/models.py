import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
from django.db import models

class Ticket(models.Model):
    customer=models.ForeignKey('customer.Customer', on_delete=models.CASCADE,null=True, blank=True)
    flight_id=models.ForeignKey('flight.Flight', on_delete=models.CASCADE,null=True, blank=True)
    cost=models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    purchase_date=models.DateField()

def __str__(self):
        return self.title

