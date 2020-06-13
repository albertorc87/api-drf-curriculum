"""Search URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from search import views

router = DefaultRouter()
router.register(r'search', views.SearchViewSet, basename='search')

urlpatterns = [
    path('', include(router.urls))
]