"""View module for handling requests about user-created words"""
from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.models.EventMarker import Eventmarker  # pylint:disable=imported-auth-user

class EventmarkerSerializer(serializers.ModelSerializer):
    """JSON serializer for Eventmarkers"""

    class Meta:
        model = Eventmarker
        url = serializers.HyperlinkedIdentityField(
            view_name='eventmarker', lookup_field='eventmarkerid'
        )
        fields = ('eventmarkerid','experimentid', 'sequencenumber','name','description', 'timestamp')
        depth = 3
        #depth=3 allows retrieval of related tables nested within parent table



class EventmarkerView(ViewSet):
    """Request Handlers for 'Eventmarker' instances in the Wave Explorer application"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    """Wave Explorer Eventmarkers"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Eventmarker

        Returns:
            Response -- JSON serialized Eventmarker
        """
        try:
            experiment = Eventmarker.objects.get(pk=pk)
            serializer = EventmarkerSerializer(
                experiment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all Eventmarkers belonging to current Plate - 'plateid'

        Returns:
            Response -- JSON serialized list of Eventmarkers
        """
        # limitting queryset to return only the first 10 objects in table
        experiment = Eventmarker.objects.all()
        serializer = EventmarkerSerializer(
            experiment, many=True, context={'request': request})
        return Response(serializer.data)