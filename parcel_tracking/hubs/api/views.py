from rest_framework import viewsets

from .serializers import HubSerializer
from parcel_tracking.hubs.models import Hub


class HubListViewSet(viewsets.ModelViewSet):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer
