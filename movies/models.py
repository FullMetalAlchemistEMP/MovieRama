from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.title

    class Meta:
        constraints = [models.UniqueConstraint(Lower("title"), name="unique_lower_title")]


class Vote(models.Model):
    VOTE_CHOICES = (
        ("like", "Like"),
        ("hate", "Hate"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="votes")
    vote_type = models.CharField(max_length=4, choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "movie")  # Ensures one vote per movie per user

    def __str__(self):
        return f"{self.user.username} - {self.vote_type} - {self.movie.title}"
