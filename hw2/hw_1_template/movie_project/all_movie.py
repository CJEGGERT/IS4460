import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()
from movie.models import Movie


all_movie= Movie.objects.all()
for m in all_movie:
    print(m.title)
