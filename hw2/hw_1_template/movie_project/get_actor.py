import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()
from actor.models import Actor

a_actor = Actor.objects.get(id=6)
print(a_actor.first_name)
print(a_actor.last_name)