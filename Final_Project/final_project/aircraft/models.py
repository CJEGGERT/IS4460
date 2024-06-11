import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
from django.db import models

class Aircraft(models.Model):
    type = models.CharField(max_length=100,null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)


def __str__(self):
        return self.type