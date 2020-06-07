"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('experiences.urls', 'experience'), namespace='experience')),
    path('', include(('education.urls', 'education'), namespace='education')),
    path('', include(('projects.urls', 'projects'), namespace='projects')),
    path('', include(('extras.urls', 'extras'), namespace='extras')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
