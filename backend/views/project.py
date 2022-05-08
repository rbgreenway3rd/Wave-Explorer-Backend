from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.models.Project import Project


class ProjectSerializer(serializers.ModelSerializer):
    """JSON serializer for Projects"""
    class Meta:
        model = Project
        url = serializers.HyperlinkedIdentityField(
            view_name='project', lookup_field='projectid')
        fields = ('projectid', 'description', 'archived', 'timestamp')
        depth = 1

class ProjectView(ViewSet):
    """Request handlers for Projects in the Wave Explorer Application"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single Project

        Returns:
            Response -- JSON serialized Project
        """
        try:
            # The '.get()' method will raise an exception if the queryset contains more than one object
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(
                project, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all projects

        Returns:
            Response -- JSON serialized list of projects
        """
        project = Project.objects.all() 
        # Note: The `many=True` argument in the serializer.
        # Needed when serializing a list of objects instead of a single object.
        serializer = ProjectSerializer(
            project, many=True, context={'request': request})
        return Response(serializer.data)