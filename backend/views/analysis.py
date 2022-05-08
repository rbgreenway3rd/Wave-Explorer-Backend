"""View module for handling requests about user-created words"""
from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.models.Analysis import Analysis  # pylint:disable=imported-auth-user

class AnalysisSerializer(serializers.ModelSerializer):
    """JSON serializer for Analysis"""

    class Meta:
        model = Analysis
        url = serializers.HyperlinkedIdentityField(
            view_name='analysis', lookup_field='analysisid'
        )
        fields = ('analysisid', 'experimentindicatorid', 'description', 'timestamp', 'runtimeanalysis', 'controlwellstring', 'numfoframes', 'dynamicrationumeratorid', 'dynamicratiodenominatorid', 'maskid'  )
        depth = 4
        #depth=3 allows retrieval of related tables nested within parent table



class AnalysisView(ViewSet):
    """Request Handlers for 'Analysis' instances in the Wave Explorer application"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    """Wave Explorer Analysiss"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Analysis

        Returns:
            Response -- JSON serialized Analysis
        """
        try:
            experiment = Analysis.objects.get(pk=pk)
            serializer = AnalysisSerializer(
                experiment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all Analysis belonging to current Plate - 'plateid'

        Returns:
            Response -- JSON serialized list of Analysis
        """
        # limitting queryset to return only the first 10 objects in table
        experiment = Analysis.objects.all()
        serializer = AnalysisSerializer(
            experiment, many=True, context={'request': request})
        return Response(serializer.data)