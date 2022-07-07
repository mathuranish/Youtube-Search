from rest_framework import serializers
from .models import APIKeys


class APIKeySerializer(serializers.ModelSerializer):

    # serialising model data
    class Meta:
        model = APIKeys
        fields = ["id", "key", "created"]
