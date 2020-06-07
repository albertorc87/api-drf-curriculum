
# Django REST Framework
from rest_framework import serializers
# Model
from projects.models import Project

class ProjectModelSerializer(serializers.ModelSerializer):
    """Projects Model Serializer"""

    class Meta:
        """Meta class."""

        model = Project
        fields = (
            'pk',
            'date',
            'title',
            'url',
            'description',
        )

class ProjectSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date = serializers.DateTimeField()
    title = serializers.CharField(max_length=255)
    url = serializers.URLField(required=False)
    description = serializers.CharField(max_length=5000)

    def create(self, data):

        pro = Project.objects.create(**data)
        return pro