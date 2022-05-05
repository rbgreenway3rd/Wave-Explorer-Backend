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
            view_name='Project', lookup_field='id')
        fields = ('PlateID', 'Project', 'OwnerID', 'Barcode',
                  'PlateTypeID', 'Description', 'IsPublic')
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
            plate = Plate.objects.get(pk=pk)
            serializer = PlateSerializer(
                plate, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    # def list(self, request):
    #     """Handle GET requests to get all created_words authored by current user

    #     Returns:
    #         Response -- JSON serialized list of created_words
    #     """
    #     user_id = request.auth.user.id
    #     user_created_words = CreatedWords.objects.filter(
    #         user=user_id)
    #     # Note the additional `many=True` argument to the
    #     # serializer. It's needed when you are serializing
    #     # a list of objects instead of a single object.
    #     serializer = CreatedWordsSerializer(
    #         user_created_words, many=True, context={'request': request})
    #     return Response(serializer.data)
