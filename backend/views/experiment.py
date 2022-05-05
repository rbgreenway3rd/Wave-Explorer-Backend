"""View module for handling requests about user-created words"""
from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from backend.models.Experiment import Experiment  # pylint:disable=imported-auth-user

class ExperimentSerializer(serializers.ModelSerializer):
    """JSON serializer for Experiments"""

    class Meta:
        model = Experiment
        url = serializers.HyperlinkedIdentityField(
            view_name='plate', lookup_field='id'
        )
        fields = ('id', 'Plate', 'MethodID', 'TimeStamp', 'Description', 'HorzBinning', 'VertBinning', 'ROI_Origin_X', 'ROI_Origin_Y', 'ROI_Width', 'ROI_Height' )
        depth = 1


class ExperimentView(ViewSet):
    """Request Handlers for 'Experiment' instances in the Wave Explorer application"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    """Wave Explorer Experiments"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Experiment

        Returns:
            Response -- JSON serialized Experiment
        """
        try:
            experiment = Experiment.objects.get(pk=pk)
            serializer = ExperimentSerializer(
                experiment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    # def list(self, request):
    #     """Handle GET requests to get all Experiments belonging to current Plate - 'plateid'

    #     Returns:
    #         Response -- JSON serialized list of Experiments
    #     """
    #     plateid = request.models.user.id
    #     user_created_words = CreatedWords.objects.filter(
    #         user=user_id)
    #     # Note the additional `many=True` argument to the
    #     # serializer. It's needed when you are serializing
    #     # a list of objects instead of a single object.
    #     serializer = CreatedWordsSerializer(
    #         user_created_words, many=True, context={'request': request})
    #     return Response(serializer.data)