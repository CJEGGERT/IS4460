from django.db import models

# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    img_url = models.TextField(null=True, blank=True)