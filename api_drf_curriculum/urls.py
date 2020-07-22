"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('experiences.urls', 'experience'), namespace='experience')),
    path('', include(('education.urls', 'education'), namespace='education')),
    path('', include(('projects.urls', 'projects'), namespace='projects')),
    path('', include(('extras.urls', 'extras'), namespace='extras')),
    path('', include(('search.urls', 'search'), namespace='search')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
