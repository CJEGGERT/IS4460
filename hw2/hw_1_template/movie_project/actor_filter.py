import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()
from actor.models import Actor

results= Actor.objects.filter(last_name__startswith=("Dica"))

print(f" First Name: {results[0].first_name}")
print(f" Last Name: {results[0].last_name}")
