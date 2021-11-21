from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for users.
    Arguments:
        serializers
    """
    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name="user",
            lookup_field="id"
        )
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "date_joined",
            "email",
            "last_login",
            'is_staff',
        )