
# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

#Serializers
from experiences.serializers import (ExperienceModelSerializer, ExperienceSerializer)

class ExperienceViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = ExperienceModelSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]
        return [p() for p in permissions]

        
    def create(self, request, *args, **kwargs):
        serializer = ExperienceSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = ExperienceModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)
    