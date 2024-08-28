from rest_framework import serializers
from ..models import Hub


class HubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hub
        fields = [
            "id",
            "name",
            "address",
            "city",
            "province",
            "zipcode",
            "full_address",
        ]
