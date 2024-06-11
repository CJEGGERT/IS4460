import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
from django.db import models

class Customer(models.Model):
    title = models.CharField(max_length=10,null=True, blank=True)
    firstName = models.CharField(max_length=50,null=True, blank=True)
    lastName = models.CharField(max_length=50,null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    citizenship = models.CharField(max_length=50,null=True, blank=True)
    email = models.CharField(max_length=30,null=True, blank=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"



