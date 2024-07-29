from rest_framework import serializers

from .models import Hub


class HubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hub
        fields = ["name", "address", "city", "postal_code", "country", 'full_address']

        def get_full_address(self, obj):
            return obj.full_address