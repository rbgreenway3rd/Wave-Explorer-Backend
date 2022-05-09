"""View module for handling requests about user-created words"""
from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.models.ExperimentImage import Experimentimage  # pylint:disable=imported-auth-user

class ExperimentimageSerializer(serializers.ModelSerializer):
    """JSON serializer for Experimentimages"""

    class Meta:
        model = Experimentimage
        url = serializers.HyperlinkedIdentityField(
            view_name='experimentimage', lookup_field='experimentimageid'
        )
        fields = ('experimentimageid','timestamp', 'experimentindicatorid', 'msecs', 'maxpixelvalue', 'compressionalgorithm', 'filepath' )
        depth = 4
        #depth=3 allows retrieval of related tables nested within parent table



class ExperimentimageView(ViewSet):
    """Request Handlers for 'Experimentimage' instances in the Wave Explorer application"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    """Wave Explorer Experimentimages"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Experimentimage

        Returns:
            Response -- JSON serialized Experimentimage
        """
        try:
            experiment = Experimentimage.objects.get(pk=pk)
            serializer = ExperimentimageSerializer(
                experiment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all Experimentimages belonging to current Plate - 'plateid'

        Returns:
            Response -- JSON serialized list of Experimentimages
        """
        # limitting queryset to return only the first 10 objects in table
        experiment = Experimentimage.objects.all().order_by('experimentimageid')[:10]
        serializer = ExperimentimageSerializer(
            experiment, many=True, context={'request': request})
        return Response(serializer.data)