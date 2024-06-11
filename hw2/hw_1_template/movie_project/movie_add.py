import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')
django.setup()
from movie.models import Movie

movies = {
    "Inception" : Movie(
        id=1,
        title="Inception", 
        description="Confusing Ass Sci-Fi Movie", 
        director="Christopher Nolan", 
        budget=160000000, 
        runtime=148, 
        genre="Science Fiction", 
        youtube_url="https://www.youtube.com/watch?v=YoHD9XEInc0", 
        img_url="https://m.media-amazon.com/images/I/71uKM+LdgFL._AC_UF894,1000_QL80_.jpg", 
        release_year=2010, 
        rating="pg-13"),

    "Monkeyman" : Movie(
        id=2,
        title="Monkeyman", 
        description="Action packed revenge flick that is like John Wick but way better", 
        director="Dev Patel", 
        budget=10000000, 
        runtime=121, 
        genre="Action Thriller", 
        youtube_url="https://www.youtube.com/watch?v=g8zxiB5Qhsc", 
        img_url="https://m.media-amazon.com/images/I/510JZ8ZTNYL._AC_UF894,1000_QL80_.jpg", 
        release_year=2024, 
        rating="R"),

    "Everything Everywhere All At Once" : Movie(
        id=3,
        title="Everything Everywhere All At Once", 
        description="Mind bending Sci Fi film about a donut", 
        director="Daniel Kwan", 
        budget=25000000, 
        runtime=139, 
        genre="Absurdist Comedy Drama", 
        youtube_url="https://www.youtube.com/watch?v=wxN1T1uxQ2g", 
        img_url="https://upload.wikimedia.org/wikipedia/en/1/1e/Everything_Everywhere_All_at_Once.jpg", 
        release_year=2022, 
        rating="R"),

    "Avater" : Movie(
        id=4,
        title="Avatar", 
        description="Space Film of humans doing human things", 
        director="James Cameron", 
        budget=237000000, 
        runtime=162, 
        genre="Science Fiction", 
        youtube_url="https://www.youtube.com/watch?v=5PSNL1qE6VY", 
        img_url="https://upload.wikimedia.org/wikipedia/en/d/d6/Avatar_%282009_film%29_poster.jpg", 
        release_year=2009, 
        rating="Pg-13"),

        "The Big Lebowski" : Movie(
        id=5,
        title="The Big Lebowski", 
        description="Famous Bowling Movie", 
        director="Joel Coen", 
        budget=15000000, 
        runtime=117, 
        genre="Crime Comedy", 
        youtube_url="https://www.youtube.com/watch?v=VgSqm8-wXWA", 
        img_url="https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg", 
        release_year=1998, 
        rating="R"),

        "Tag" : Movie(
        id=6,
        title="Tag", 
        description="A group of friends who never grew up and plays tag year after year", 
        director="Jeff Tomsic", 
        budget=28000000, 
        runtime=101, 
        genre="Comedy", 
        youtube_url="https://www.youtube.com/watch?v=kjC1zmZo30U", 
        img_url="https://upload.wikimedia.org/wikipedia/en/6/6f/Tag_%282018_film%29.png", 
        release_year=2018, 
        rating="R"),

        "Star Wars: A New Hope" : Movie(
        id=7,
        title="Star Wars: A New Hope", 
        description="Star family has argument about whether or not to take over the galaxy", 
        director="George Lucas", 
        budget=11000000, 
        runtime=121, 
        genre="Epic Space Opera", 
        youtube_url="https://www.youtube.com/watch?v=vZ734NWnAHA", 
        img_url="https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg", 
        release_year=1977, 
        rating="Pg"),

        "Good Will Hunting" : Movie(
        id=8,
        title="Good Will Hunting", 
        description="Smart guy has temper tantrum because he doesn't want to put in effort", 
        director="Gus Van Sant", 
        budget=10000000, 
        runtime=126, 
        genre="Drama", 
        youtube_url="https://www.youtube.com/watch?v=ReIJ1lbL-Q8", 
        img_url="https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png", 
        release_year=1997, 
        rating="R"),

        "Miracle" : Movie(
        id=9,
        title="Miracle", 
        description="US Hockey Team beats Russia despite the Russians Ice Skating for daily transportaion", 
        director="Gavin O'Connor", 
        budget=28000000, 
        runtime=136, 
        genre="Sports", 
        youtube_url="https://www.youtube.com/watch?v=Bd0_Dm2xlEM", 
        img_url="https://upload.wikimedia.org/wikipedia/en/5/55/Miracle_film.jpg", 
        release_year=2004, 
        rating="Pg"),

        "The Shawshank Redemption" : Movie(
        id=10,
        title="The Shawshank Redemption", 
        description="Man goes to Prison. He probably did it", 
        director="Frank Darabont", 
        budget=25000000, 
        runtime=142, 
        genre="Drama", 
        youtube_url="https://www.youtube.com/watch?v=PLl99DlL6b4", 
        img_url="https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", 
        release_year=1994, 
        rating="R"),    
}


for movie_key in movies.keys():
    print(movie_key)
    movie = movies.get(movie_key)
    movie.save()
