"""View module for handling requests about user-created words"""
from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.models.ExperimentIndicator import Experimentindicator  # pylint:disable=imported-auth-user

class ExperimentindicatorSerializer(serializers.ModelSerializer):
    """JSON serializer for Experimentindicators"""

    class Meta:
        model = Experimentindicator
        url = serializers.HyperlinkedIdentityField(
            view_name='experimentindicator', lookup_field='experimentindicatorid'
        )
        fields = ('experimentindicatorid','experimentid', 'excitationfilterdesc', 'emissionfilterdesc', 'excitationfilterpos', 'emissionfilterpos', 'maskid', 'exposure', 'gain', 'preampgain', 'description', 'signaltype', 'flatfieldcorrection' )
        depth = 3
        #depth=3 allows retrieval of related tables nested within parent table



class ExperimentindicatorView(ViewSet):
    """Request Handlers for 'Experimentindicator' instances in the Wave Explorer application"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    """Wave Explorer Experimentindicators"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Experimentindicator

        Returns:
            Response -- JSON serialized Experimentindicator
        """
        try:
            experiment = Experimentindicator.objects.get(pk=pk)
            serializer = ExperimentindicatorSerializer(
                experiment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all Experimentindicators belonging to current Plate - 'plateid'

        Returns:
            Response -- JSON serialized list of Experimentindicators
        """
        experiment = Experimentindicator.objects.all()
        serializer = ExperimentindicatorSerializer(
            experiment, many=True, context={'request': request})
        return Response(serializer.data)