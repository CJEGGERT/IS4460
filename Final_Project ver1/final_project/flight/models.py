import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
from django.db import models

class Flight(models.Model):
    airport_to = models.ForeignKey('airport.Airport', related_name='arriving_flights', on_delete=models.CASCADE)
    airport_from = models.ForeignKey('airport.Airport', related_name='departing_flights', on_delete=models.CASCADE)
    aircraft = models.ForeignKey('aircraft.Aircraft', on_delete=models.CASCADE,null=True, blank=True)
    departure_date=models.DateField(null=True, blank=True)
    departure_time=models.TimeField(null=True, blank=True)
    departure_gate=models.IntegerField(null=True, blank=True)
    arrival_gate=models.IntegerField(null=True, blank=True)
    duration_min=models.IntegerField(null=True, blank=True)
    emmployee=models.ManyToManyField('employee.Employee', through='FlightEmployee')

    def __str__(self):
        return f"Flight from {self.airport_from} to {self.airport_to}"
    
class FlightEmployee(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee} on {self.flight}"