
# Django REST Framework
from rest_framework import serializers
# Model
from experiences.models import Experience

class ExperienceModelSerializer(serializers.ModelSerializer):
    """Experience Model Serializer"""

    class Meta:
        """Meta class."""

        model = Experience
        fields = (
            'pk',
            'date_ini',
            'date_end',
            'company',
            'description',
        )

class ExperienceSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_ini = serializers.DateTimeField()
    date_end = serializers.DateTimeField(required=False)
    company = serializers.CharField(max_length=250)
    description = serializers.CharField(max_length=10000)

    def create(self, data):

        exp = Experience.objects.create(**data)
        return exp