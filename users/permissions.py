"""User permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from users.models import User


class IsStandardUser(BasePermission):
    """Allow access to create experience, extras and projects."""

    def has_permission(self, request, view):

        try:
            user = User.objects.get(
                email=request.user,
                is_recruiter=False
            )
        except User.DoesNotExist:
            return False
        return True


class IsRecruiterUser(BasePermission):
    """Allow access to search curriculums."""

    def has_permission(self, request, view):

        try:
            user = User.objects.get(
                email=request.user,
                is_recruiter=True
            )
        except User.DoesNotExist:
            return False
        return True