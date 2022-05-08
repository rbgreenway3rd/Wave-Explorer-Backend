from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.models.User import User


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for Users"""
    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='user', lookup_field='userid')
        fields = ('userid', 'firstname', 'lastname', 'username', 'password', 'role')
        depth = 1

class UserView(ViewSet):
    """Request handlers for Users in the Wave Explorer Application"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single User

        Returns:
            Response -- JSON serialized User
        """
        try:
            # The '.get()' method will raise an exception if the queryset contains more than one object
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(
                user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """
        user = User.objects.all() 
        # Note: The `many=True` argument in the serializer.
        # Needed when serializing a list of objects instead of a single object.
        serializer = UserSerializer(
            user, many=True, context={'request': request})
        return Response(serializer.data)