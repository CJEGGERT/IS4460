import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()
from movie.models import Movie

results= Movie.objects.filter(title__startswith=("Inception"))

print(f" the movie is: {results[0]}")
