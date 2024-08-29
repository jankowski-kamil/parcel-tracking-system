from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import HubSerializer
from parcel_tracking.hubs.models import Hub
from ...permissions.staff_permissions import IsStaff


class HubListViewSet(viewsets.ModelViewSet):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer
    permission_classes = [IsAuthenticated, IsStaff]
