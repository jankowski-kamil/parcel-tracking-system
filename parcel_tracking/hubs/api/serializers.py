from rest_framework import serializers
from ..models import Hub


class HubSerializer(serializers.ModelSerializer):
    full_address = serializers.SerializerMethodField(read_only=True)
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
