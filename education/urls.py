"""Education URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from education import views

router = DefaultRouter()
router.register(r'education', views.EducationViewSet, basename='education')

urlpatterns = [
    path('', include(router.urls))
]