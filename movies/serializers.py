from rest_framework import serializers
from .models import Movie, Vote
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class MovieSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField()
    hates = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'created_at', 'user', 'likes', 'hates']

    def get_likes(self, obj):
        return obj.votes.filter(vote_type='like').count()

    def get_hates(self, obj):
        return obj.votes.filter(vote_type='hate').count()

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'movie', 'vote_type', 'created_at']
