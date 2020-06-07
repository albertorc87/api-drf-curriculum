
# Django REST Framework
from rest_framework import serializers
# Model
from extras.models import Extra

class ExtraModelSerializer(serializers.ModelSerializer):
    """Extras Model Serializer"""

    class Meta:
        """Meta class."""

        model = Extra
        fields = (
            'pk',
            'expedition',
            'title',
            'url',
            'description',
        )

class ExtraSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    expedition = serializers.DateTimeField()
    title = serializers.CharField(max_length=255)
    url = serializers.URLField(required=False)
    description = serializers.CharField(max_length=5000)

    def create(self, data):

        extra = Extra.objects.create(**data)
        return extra