import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()
from actor.models import Actor  

actors= {

        "Leonardo_Dicaprio" : Actor (
                id=1,
                first_name = "Leonardo",
                last_name = "Dicaprio",
                img_url = "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQca59lIsX6cXLNmRMle2fcCkURB4AvtkSqh-4Do1NwxEW49fNW"
                ),

            "Dev_Patel" : Actor (
                id=2,
                first_name = "Dev",
                last_name = "Patel",
                img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0fQ3DywBO3Gzpr5AuKHYRG_zvXkq5E71z0A&s",
                ),

            "Michelle_Yeoh" : Actor (
                id=3,
                first_name = "Michelle",
                last_name = "Yeoh",
                img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Michelle_Yeoh_at_EC_%282023%29_2.jpg/440px-Michelle_Yeoh_at_EC_%282023%29_2.jpg",
                ),
            
            "Sam_Worthington" : Actor (
                id=4,
                first_name = "Sam",
                last_name = "Worthington",
                img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHopGbZ0ZEi3NRYlVm4Wdh4cDzGbl-UqRD7g&s",
                ),

            "Jeff_Bridges" : Actor (
                id=5,
                first_name = "Jeff",
                last_name = "Bridges",
                img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Jeff_Bridges_by_Gage_Skidmore_3.jpg/440px-Jeff_Bridges_by_Gage_Skidmore_3.jpg",
                ),

            "Jeremy_Renner" : Actor (
                id=6,
                first_name = "Jeremy",
                last_name = "Renner",
                img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Jeremy_Renner_by_Gage_Skidmore_2.jpg/440px-Jeremy_Renner_by_Gage_Skidmore_2.jpg",
                ),

            "Mark_Hamil" : Actor (
                id=7,
                first_name = "Mark",
                last_name = "Hamil",
                img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Mark_Hamill_by_Gage_Skidmore_2.jpg/440px-Mark_Hamill_by_Gage_Skidmore_2.jpg",
                ),

            "Robin_Williams" : Actor (
                id=8,
                first_name = "Robin",
                last_name = "Williams",
                img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Robin_Williams_1978_%28cropped%29.jpg/440px-Robin_Williams_1978_%28cropped%29.jpg",
                ),

            "Kurt_Russel" : Actor (
                id=9,
                first_name = "Kurt",
                last_name = "Russel",
                img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Kurt_Russell_by_Gage_Skidmore_2.jpg/440px-Kurt_Russell_by_Gage_Skidmore_2.jpg",
                ),

            "Morgan_Freeman" : Actor (
                id=10,
                first_name = "Morgan",
                last_name = "Freeman",
                img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Morgan_Freeman_at_The_Pentagon_on_2_August_2023_-_230802-D-PM193-3363_%28cropped%29.jpg/440px-Morgan_Freeman_at_The_Pentagon_on_2_August_2023_-_230802-D-PM193-3363_%28cropped%29.jpg",
                ),         
}

for actor_key in actors.keys():
    print(actor_key)
    actor = actors.get(actor_key)
    actor.save()