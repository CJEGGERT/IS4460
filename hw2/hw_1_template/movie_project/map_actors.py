import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()
from movie.models import Movie
from movie.models import Actor

actor_mappings = {
    "Inception" : ("Leonardo", "Dicaprio"),
    "Monkeyman" : ("Dev", "Patel"),
    "Everything Everywhere All At Once" : ("Michelle","Yeoh"),
    "Avatar" : ("Sam","Worthington"),
    "The Big Lebowski" : ("Jeff","Bridges"),
    "Tag" : ("Jeremy","Renner"),
    "Star Wars: A New Hope" : ("Mark","Hamil"),
    "Good Will Hunting" : ("Robin","Williams"),
    "Miracle" : ("Kurt","Russel"),
    "The Shawshank Redemption" : ("Morgan","Freeman")
}

for movie_name in actor_mappings.keys():
    actor_tuple = actor_mappings.get(movie_name)
    print("Adding actors for movie " + movie_name)
    movie = Movie.objects.get(title=movie_name)
    actor = Actor.objects.get(first_name=actor_tuple[0], last_name=actor_tuple[1])
    movie.actor.add(actor)


