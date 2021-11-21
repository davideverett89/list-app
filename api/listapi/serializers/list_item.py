from rest_framework import serializers
from listapi.models import List

class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for lists.
    Arguments:
        serializers
    """
    class Meta:
        model = List
        url = serializers.HyperlinkedIdentityField(
            view_name="list",
            lookup_field="id"
        )
        fields = (
            "id",
            "name",
            "description"
            "list_id"
        )