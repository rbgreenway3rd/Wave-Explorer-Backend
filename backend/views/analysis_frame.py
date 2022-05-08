"""View module for handling requests about user-created words"""
from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.models.AnalysisFrame import Analysisframe  # pylint:disable=imported-auth-user

class AnalysisFrameSerializer(serializers.ModelSerializer):
    """JSON serializer for Analysis"""

    class Meta:
        model = Analysisframe
        url = serializers.HyperlinkedIdentityField(
            view_name='analysisframe', lookup_field='analysisframeid'
        )
        fields = ('analysisframeid', 'analysisid', 'sequencenumber', 'rows', 'cols', 'valuestring'  )
        depth = 1
        #depth=3 allows retrieval of related tables nested within parent table



class AnalysisFrameView(ViewSet):
    """Request Handlers for 'Analysis frame' instances in the Wave Explorer application"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    """Wave Explorer Analysis frames"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Analysis frame

        Returns:
            Response -- JSON serialized Analysis frame
        """
        try:
            experiment = Analysisframe.objects.get(pk=pk)
            serializer = AnalysisFrameSerializer(
                experiment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all Analysis frame belonging to current Plate - 'plateid'

        Returns:
            Response -- JSON serialized list of Analysis frame
        """
        # limitting queryset to return only the first 10 objects in table
        experiment = Analysisframe.objects.all().order_by('analysisframeid')[:10]
        serializer = AnalysisFrameSerializer(
            experiment, many=True, context={'request': request})
        return Response(serializer.data)