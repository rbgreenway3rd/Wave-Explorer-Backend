"""View module for handling requests about user-created words"""
from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.models.ExperimentCompoundPlate import Experimentcompoundplate  # pylint:disable=imported-auth-user

class ExperimentcompoundplateSerializer(serializers.ModelSerializer):
    """JSON serializer for Experimentcompoundplates"""

    class Meta:
        model = Experimentcompoundplate
        url = serializers.HyperlinkedIdentityField(
            view_name='experimentimage', lookup_field='experimentimageid'
        )
        fields = ('experimentcompoundplateid', 'description', 'barcode', 'experimentid')
        depth = 3
        #depth=3 allows retrieval of related tables nested within parent table



class ExperimentcompoundplateView(ViewSet):
    """Request Handlers for 'Experimentcompoundplate' instances in the Wave Explorer application"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    """Wave Explorer Experimentcompoundplates"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Experimentcompoundplate

        Returns:
            Response -- JSON serialized Experimentcompoundplate
        """
        try:
            experiment = Experimentcompoundplate.objects.get(pk=pk)
            serializer = ExperimentcompoundplateSerializer(
                experiment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all Experimentcompoundplates belonging to current Plate - 'plateid'

        Returns:
            Response -- JSON serialized list of Experimentcompoundplates
        """
        # limitting queryset to return only the first 10 objects in table
        experiment = Experimentcompoundplate.objects.all()
        serializer = ExperimentcompoundplateSerializer(
            experiment, many=True, context={'request': request})
        return Response(serializer.data)