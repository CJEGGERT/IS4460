import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()
from actor.models import Actor


all_actor= Actor.objects.all()
for a in all_actor:
    print(a.first_name, a.last_name)