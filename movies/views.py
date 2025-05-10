from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from rest_framework import viewsets, permissions
from .models import Movie, Vote
from .serializers import MovieSerializer, VoteSerializer
from rest_framework.exceptions import PermissionDenied

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.db.models import Count, Q, Case, When, Value, F, FloatField, ExpressionWrapper
from django.db.models import OuterRef, Subquery


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


class MovieListView(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    context_object_name = "movies"
    paginate_by = 5

    def get_queryset(self):
        qs = Movie.objects.all()
        qs = self._annotate_votes(qs)
        qs = self._annotate_rating(qs)
        qs = self._annotate_user_vote(qs, self.request.user)

        user_id = self.request.GET.get("user_id")
        if user_id:
            qs = qs.filter(user_id=user_id)

        qs = self._apply_sorting(qs)
        return qs

    def _annotate_votes(self, qs):
        return qs.annotate(
            likes=Count("votes", filter=Q(votes__vote_type="like")),
            hates=Count("votes", filter=Q(votes__vote_type="hate")),
        )

    def _annotate_rating(self, qs):
        return qs.annotate(
            total_votes=F("likes") + F("hates"),
            rating=Case(
                When(
                    likes__gt=0,
                    then=ExpressionWrapper(
                        (F("likes") * 100.0) / (F("likes") + F("hates")), output_field=FloatField()
                    ),
                ),
                When(
                    hates__gt=0,
                    then=ExpressionWrapper(
                        (F("likes") * 100.0) / (F("likes") + F("hates")), output_field=FloatField()
                    ),
                ),
                default=Value(None),
                output_field=FloatField(),
            ),
        )

    def _annotate_user_vote(self, qs, user):
        if user.is_authenticated:
            vote_subquery = Vote.objects.filter(movie=OuterRef("pk"), user=user).values(
                "vote_type"
            )[:1]
            return qs.annotate(user_vote=Subquery(vote_subquery))
        return qs

    def _apply_sorting(self, qs):
        sort = self.request.GET.get("sort")
        if sort == "likes":
            return qs.order_by("-likes", "-created_at")
        elif sort == "hates":
            return qs.order_by("-hates", "-created_at")
        elif sort == "rating":
            return qs.order_by("-rating", "-created_at")
        return qs.order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.GET.get("user_id")
        if user_id:
            context["filter_user"] = User.objects.filter(id=user_id).first()

        sort = self.request.GET.get("sort", "date")
        context["current_sort"] = sort
        context["movie_count"] = self.get_queryset().count()
        return context


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ["title", "description"]
    template_name = "movies/movie_form.html"
    success_url = reverse_lazy("movie-list-view")
    login_url = "login"  # ensures redirect to login page if unauthenticated

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class MovieViewSet(viewsets.ModelViewSet):
    # Retrieve all movies, ordered by newest first
    queryset = Movie.objects.all().order_by("-created_at")
    serializer_class = MovieSerializer
    # Unauthenticated users can read, only authenticated users can write
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post"]

    def perform_create(self, serializer):
        # Automatically associate the current user with the created movie
        serializer.save(user=self.request.user)


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    # Only authenticated users can access this viewset
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post"]

    def get_queryset(self):
        # Only return votes by the currently authenticated user
        return Vote.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Prevent users from voting on their own movies
        movie = serializer.validated_data["movie"]

        if movie.user == self.request.user:
            raise PermissionDenied("You cannot vote on your own movie.")

        serializer.save(user=self.request.user)


@require_POST
@login_required
def vote_view(request):
    movie = get_object_or_404(Movie, id=request.POST["movie_id"])

    if movie.user == request.user:
        return redirect(request.META.get("HTTP_REFERER", "movie-list-view"))

    vote_type = request.POST["vote_type"]
    existing_vote = Vote.objects.filter(user=request.user, movie=movie).first()

    if existing_vote:
        if existing_vote.vote_type == vote_type:
            existing_vote.delete()  # Retract vote
        else:
            existing_vote.vote_type = vote_type  # Switch vote
            existing_vote.save()
    else:
        Vote.objects.create(user=request.user, movie=movie, vote_type=vote_type)

    return redirect(request.META.get("HTTP_REFERER", "movie-list-view"))
