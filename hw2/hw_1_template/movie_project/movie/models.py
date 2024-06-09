from django.db import models

# Create your models here.

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    rating = models.CharField(max_length=50, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    youtube_url = models.TextField(null=True, blank=True)
    img_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
