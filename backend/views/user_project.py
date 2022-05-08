from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.models.UserProject import Userproject


class UserProjectSerializer(serializers.ModelSerializer):
    """JSON serializer for UserProjects"""
    class Meta:
        model = Userproject
        url = serializers.HyperlinkedIdentityField(
            view_name='userproject', lookup_field='projectid')
        fields = ('userid', 'projectid')
        depth = 2

class UserProjectView(ViewSet):
    """Request handlers for UserProjects in the Wave Explorer Application"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single UserProject

        Returns:
            Response -- JSON serialized UserProject
        """
        try:
            # The '.get()' method will raise an exception if the queryset contains more than one object
            user = Userproject.objects.get(pk=pk)
            serializer = UserProjectSerializer(
                user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """
        user = Userproject.objects.all() 
        # Note: The `many=True` argument in the serializer.
        # Needed when serializing a list of objects instead of a single object.
        serializer = UserProjectSerializer(
            user, many=True, context={'request': request})
        return Response(serializer.data)