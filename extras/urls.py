"""Extras URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from extras import views

router = DefaultRouter()
router.register(r'extras', views.ExtraViewSet, basename='extras')

urlpatterns = [
    path('', include(router.urls))
]