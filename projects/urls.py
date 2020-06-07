"""Projects URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from projects import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls))
]