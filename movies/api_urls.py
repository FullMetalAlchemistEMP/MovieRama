from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, VoteViewSet, UserCreateView

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'votes', VoteViewSet, basename='vote')

urlpatterns = router.urls + [
    path('', include(router.urls)),
    path('register/', UserCreateView.as_view(), name='user-register'),
]
