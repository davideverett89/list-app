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
        """Handle GET requests for a single list
        Returns:
            Response -- JSON serialized list instance
        """
        try:
            list = List.objects.get(pk=pk)
            serializer = ListSerializer(list, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        try:
            if request.user.id:
                lists = List.objects.filter(user=request.user.id)
            else:
                lists = List.objects.all()
            serializer = ListSerializer(
                lists, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a list
        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            list = List.objects.get(pk=pk)
            list.name = request.data["name"]
            list.description = request.data["description"]
            list.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        try:
            new_list = List()
            new_list.name = request.data['name']
            new_list.description = request.data['description']
            new_list.user = User.objects.get(pk=self.request.user.id)
            new_list.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def destory(self, request, pk=None):
        try:
            list = List.objects.get(pk=pk)
            list.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except List.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)
        