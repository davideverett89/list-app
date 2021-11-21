from rest_framework import serializers
from listapi.models import ListItem

class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for lists.
    Arguments:
        serializers
    """
    class Meta:
        model = ListItem
        url = serializers.HyperlinkedIdentityField(
            view_name="list_item",
            lookup_field="id"
        )
        fields = (
            "id",
            "name",
            "description",
            "list_id",
        )