from django.test import TestCase
from django.contrib.auth.models import User
from movies.models import Movie, Vote


class MovieRamaTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="pass123")
        self.user2 = User.objects.create_user(username="user2", password="pass123")
        self.movie = Movie.objects.create(title="Test Movie", description="Test Desc", user=self.user1)

    def test_user_can_vote_like(self):
        vote = Vote.objects.create(user=self.user2, movie=self.movie, vote_type="like")
        self.assertEqual(vote.vote_type, "like")
        self.assertEqual(Vote.objects.count(), 1)

    def test_user_can_vote_hate(self):
        vote = Vote.objects.create(user=self.user2, movie=self.movie, vote_type="hate")
        self.assertEqual(vote.vote_type, "hate")
        self.assertEqual(Vote.objects.count(), 1)

    def test_user_can_switch_vote(self):
        Vote.objects.create(user=self.user2, movie=self.movie, vote_type="like")
        vote = Vote.objects.get(user=self.user2, movie=self.movie)
        vote.vote_type = "hate"
        vote.save()
        updated_vote = Vote.objects.get(user=self.user2, movie=self.movie)
        self.assertEqual(updated_vote.vote_type, "hate")
