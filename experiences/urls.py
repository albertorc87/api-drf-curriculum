"""Experience URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from experiences import views

router = DefaultRouter()
router.register(r'experience', views.ExperienceViewSet, basename='experience')

urlpatterns = [
    path('', include(router.urls))
]