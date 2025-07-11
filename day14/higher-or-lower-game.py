import random

# 20 movies from imdb:

movies = [
    {"title": "The Shawshank Redemption", "imdb": 9.3},
    {"title": "The Godfather", "imdb": 9.2},
    {"title": "The Dark Knight", "imdb": 9.0},
    {"title": "The Godfather Part II", "imdb": 9.0},
    {"title": "12 Angry Men", "imdb": 9.0},
    {"title": "Schindler's List", "imdb": 8.9},
    {"title": "The Lord of the Rings: The Return of the King", "imdb": 8.9},
    {"title": "Pulp Fiction", "imdb": 8.9},
    {"title": "The Good, the Bad and the Ugly", "imdb": 8.8},
    {"title": "Forrest Gump", "imdb": 8.8},
    {"title": "Fight Club", "imdb": 8.8},
    {"title": "Inception", "imdb": 8.8},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "imdb": 8.8},
    {"title": "Star Wars: Episode V - The Empire Strikes Back", "imdb": 8.7},
    {"title": "The Matrix", "imdb": 8.7},
    {"title": "Goodfellas", "imdb": 8.7},
    {"title": "One Flew Over the Cuckoo's Nest", "imdb": 8.7},
    {"title": "Se7en", "imdb": 8.6},
    {"title": "The Silence of the Lambs", "imdb": 8.6},
    {"title": "It's a Wonderful Life", "imdb": 8.6}
]


def play_game(movies):
    score = 0
    movie_a = random.choice(movies)
    while True:
        movie_b = random.choice(movies)
        # in khat code baraye ine ke eshtebahi 2ta item baham yeki nashe
        while movie_b == movie_a:
            movie_b = random.choice(movies)

        print(f""" compare the imdb score.
         A: {movie_a['title']} (imdb score is: {movie_a['imdb']})""")
        print(f"against B: {movie_b['title']} (imdb score is: ??)")

        guesse = input("which one has the highest score in imdb. A or B?").upper()

        score_a = movie_a["imdb"]
        score_b = movie_b["imdb"]

        if (guesse == "A" and score_a >= score_b) or (guesse == "B" and score_b >= score_a):
            score += 1
            print(f"you are right. your score is {score}")
            # hala jay movie a ba b avaz mishe
            movie_a = movie_b
        else:
            print(f"you are wrong. final score is {score}")
            break

play_game(movies)
