import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()
from actor.models import Actor

all_actor= Actor.objects.all()
for a in all_actor:
    print('Deleting ' + a.first_name + a.last_name)
    a.delete() 
