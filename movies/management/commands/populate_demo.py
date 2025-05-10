from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from movies.models import Movie, Vote
import random


class Command(BaseCommand):
    help = "Populate demo users and movies with IMDb-style descriptions"

    def handle(self, *args, **kwargs):
        # Clear demo users, votes, and movies
        self.stdout.write("🧹 Clearing old demo data...")
        Vote.objects.all().delete()
        Movie.objects.all().delete()
        User.objects.filter(username__startswith="user").delete()

        # Create 10 users
        users = []
        for i in range(1, 21):
            username = f"user{i}"
            user, created = User.objects.get_or_create(
                username=username, defaults={"email": f"{username}@demo.com"}
            )
            user.set_password("demo123")
            user.save()
            users.append(user)

        # List of 10 sci-fi/fantasy movies with short IMDb-style descriptions
        movies_data = [
            ("The Matrix", "A computer hacker learns about the true nature of his reality."),
            ("Inception", "A thief who steals corporate secrets through dream-sharing technology."),
            (
                "Interstellar",
                "A team of explorers travel through a wormhole to ensure humanity's survival.",
            ),
            ("The Lord of the Rings", "A hobbit sets out on a journey to destroy a powerful ring."),
            ("Star Wars: A New Hope", "A farm boy joins a rebellion against an evil empire."),
            ("Blade Runner", "A blade runner must hunt down four replicants who stole a ship."),
            (
                "The Fifth Element",
                "A cab driver in the future becomes central to saving the world.",
            ),
            ("The Prestige", "Two rival magicians engage in a deadly battle of illusions."),
            ("Arrival", "A linguist is recruited to communicate with extraterrestrials."),
            ("The Hobbit", "A reluctant hobbit sets out to reclaim a treasure from a dragon."),
            ("Dune", "A young nobleman leads desert warriors against a galactic empire."),
            ("Avatar", "A paraplegic marine inhabits an alien body on a distant world."),
            ("Guardians of the Galaxy", "A band of misfits must save the galaxy from destruction."),
            (
                "Doctor Strange",
                "A surgeon turns sorcerer to protect the world from mystical threats.",
            ),
            ("Edge of Tomorrow", "A soldier relives the same day in a war against aliens."),
            (
                "The Hunger Games",
                "A girl fights for survival in a dystopian televised death match.",
            ),
            ("Chronicle", "Teens gain telekinetic powers and spiral out of control."),
            ("District 9", "Aliens are segregated in slums and face human exploitation."),
            ("Eternals", "Immortal beings defend Earth from ancient enemies."),
            ("Tenet", "A secret agent manipulates time to prevent World War III."),
        ]

        movies = []
        for title, desc in movies_data:
            user = random.choice(users)
            movie = Movie.objects.create(title=title, description=desc, user=user)
            movies.append(movie)

        # Generate votes
        for user in users:
            for movie in random.sample(movies, k=random.randint(5, len(movies_data))):
                if movie.user == user:
                    continue  # Skip self-voting
                vote_type = random.choice(["like", "like", "hate"])
                Vote.objects.get_or_create(user=user, movie=movie, vote_type=vote_type)

        self.stdout.write(self.style.SUCCESS("✅ Demo users, movies, and votes created."))
