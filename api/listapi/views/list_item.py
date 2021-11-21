"""View module for handling requests about list"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from listapi.models import ListItem, List
from listapi.serializers import ListItemSerializer

class ListItems(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single list item
        Returns:
            Response -- JSON serialized list item instance
        """
        try:
            list_item = ListItem.objects.get(pk=pk)
            serializer = ListItemSerializer(list_item, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        try:
            list_items = ListItem.objects.all()
            serializer = ListItemSerializer(
                list_items, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a list item
        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            list_item = ListItem.objects.get(pk=pk)
            list_item.name = request.data["name"]
            list_item.description = request.data["description"]
            list_item.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        try:
            new_list_item = ListItem()
            new_list_item.name = request.data['name']
            new_list_item.description = request.data['description']
            new_list_item.list = List.objects.get(pk=request.data['list_id'])
            new_list_item.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def destory(self, request, pk=None):
        try:
            list_item = ListItem.objects.get(pk=pk)
            list_item.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except ListItem.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)