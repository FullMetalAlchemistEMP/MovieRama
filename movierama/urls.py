from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK")

urlpatterns = [
    path('admin/', admin.site.urls),
    # Web UI views (login, signup, movies list)
    path('', include('movies.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # for login/logout
    # API endpoints
    path('api/', include('movies.api_urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('healthz/', health_check),
]
