import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
from django.db import models

class Airport(models.Model):
    airport_code = models.CharField(max_length=10, primary_key=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    

def __str__(self):
    return self.airport_code
