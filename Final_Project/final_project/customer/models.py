import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)