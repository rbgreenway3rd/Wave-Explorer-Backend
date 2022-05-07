from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.models.Plate import Plate


class PlateSerializer(serializers.ModelSerializer):
    """JSON serializer for Plates"""
    class Meta:
        model = Plate
        url = serializers.HyperlinkedIdentityField(
            view_name='plate', lookup_field='plateid')
        fields = ('plateid', 'projectid', 'ownerid', 'barcode',
                  'platetypeid', 'description', 'ispublic')
        depth = 1

class PlateView(ViewSet):
    """Request handlers for Plates in the Wave Explorer Application"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single Plate

        Returns:
            Response -- JSON serialized Plate
        """
        try:
            # The '.get()' method will raise an exception if the queryset contains more than one object
            plate = Plate.objects.get(pk=pk)
            serializer = PlateSerializer(
                plate, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all plates

        Returns:
            Response -- JSON serialized list of plates
        """
        plate = Plate.objects.all() 
        # Note: The `many=True` argument in the serializer.
        # Needed when serializing a list of objects instead of a single object.
        serializer = PlateSerializer(
            plate, many=True, context={'request': request})
        return Response(serializer.data)
