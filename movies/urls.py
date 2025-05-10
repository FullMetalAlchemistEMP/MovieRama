from django.urls import path
from .views import MovieListView, MovieCreateView, signup, vote_view

urlpatterns = [
    # Web UI views
    path('signup/', signup, name='signup'),
    path('movies/', MovieListView.as_view(), name='movie-list-view'),
    path('movies/add/', MovieCreateView.as_view(), name='movie-add'),
    path('vote/', vote_view, name='vote'),

]
