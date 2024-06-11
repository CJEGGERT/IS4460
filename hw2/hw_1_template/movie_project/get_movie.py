import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()
from movie.models import Movie

a_movie = Movie.objects.get(id=3)
print (a_movie.title)
