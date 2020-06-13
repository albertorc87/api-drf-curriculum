
# Django REST Framework
from rest_framework import serializers

# Models
from users.models import User
from experiences.models import Experience
from education.models import Education
from extras.models import Extra
from projects.models import Project


class ExperienceCurriculumSerializer(serializers.ModelSerializer):
    """Experience Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Experience
        fields = [
            'date_ini',
            'date_end',
            'company',
            'description',
        ]

class EducationCurriculumSerializer(serializers.ModelSerializer):
    """Education Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Education
        fields = (
            'date_ini',
            'date_end',
            'title',
        )


class ExtraCurriculumSerializer(serializers.ModelSerializer):
    """Extras Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Extra
        fields = (
            'expedition',
            'title',
            'url',
            'description',
        )


class ProjectCurriculumSerializer(serializers.ModelSerializer):
    """Projects Curriculum Model Serializer"""

    class Meta:
        """Meta class."""

        model = Project
        fields = (
            'date',
            'title',
            'url',
            'description',
        )


class CurriculumSerializer(serializers.ModelSerializer):

    experience = ExperienceCurriculumSerializer(many=True)
    education = EducationCurriculumSerializer(many=True)
    extra_education = ExtraCurriculumSerializer(many=True)
    projects = ProjectCurriculumSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'extract',
            'phone',
            'city',
            'country',
            'experience',
            'education',
            'extra_education',
            'projects',
        ]