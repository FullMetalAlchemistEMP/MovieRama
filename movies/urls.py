from django.urls import path
from .views import MovieListView, MovieCreateView, signup, vote_view
from django.views.generic import RedirectView

urlpatterns = [
    # Web UI views
    path("signup/", signup, name="signup"),
    path("movies/", MovieListView.as_view(), name="movie-list-view"),
    path("movies/add/", MovieCreateView.as_view(), name="movie-add"),
    path("vote/", vote_view, name="vote"),
    path("", RedirectView.as_view(url="/movies/", permanent=False)),
]
