"""View module for handling requests about list"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from listapi.models import List
from listapi.serializers import ListSerializer
from django.contrib.auth.models import User

class Lists(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for single list
        Returns:
            Response -- JSON serialized list instance
        """

        try:
            list = List.objects.get(pk=pk)
            serializer = ListSerializer(list, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a list
        Returns:
            Response -- Empty body with 204 status code
        """
        list = List.objects.get(pk=pk)
        list.name = request.data["name"]
        list.descriptin = request.data["description"]
        list.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request):

        if request.user.id:
            lists = List.objects.filter(user=request.user.id)

        else:
            lists = List.objects.all()

        serializer = ListSerializer(
            lists, many=True, context={'request': request})

        return Response(serializer.data)
    
    def create(self, request):
        
        