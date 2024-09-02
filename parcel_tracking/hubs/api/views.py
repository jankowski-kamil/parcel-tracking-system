from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import HubSerializer
from parcel_tracking.hubs.models import Hub
from ...permissions.staff_permissions import IsStaff
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class HubListViewSet(viewsets.ModelViewSet):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer
    permission_classes = [IsAuthenticated, IsStaff]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = "__all__"
