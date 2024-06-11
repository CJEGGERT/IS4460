import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50,null=True, blank=True)
    last_name = models.CharField(max_length=50,null=True, blank=True)
    job_title = models.CharField(max_length=50,null=True, blank=True)
    


    def __str__(self):
        return f"{self.first_name} {self.last_name}"