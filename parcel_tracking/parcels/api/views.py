from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from parcel_tracking.parcels.api.serializers import (
    ParcelAddressSerializer,
    ParcelSizeSerializer,
    ParcelSerializer,
)
from parcel_tracking.parcels.models import Parcel, ParcelAddress, ParcelSize


from parcel_tracking.permissions.staff_permissions import IsStaff


class ParcelAddressViewSet(viewsets.ModelViewSet):
    queryset = ParcelAddress.objects.all()
    permission_classes = [IsAuthenticated, IsStaff]
    serializer_class = ParcelAddressSerializer


class ParcelSizeViewSet(viewsets.ModelViewSet):
    queryset = ParcelSize.objects.all()
    permission_classes = [IsAuthenticated, IsStaff]
    serializer_class = ParcelSizeSerializer


class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    permission_classes = [IsAuthenticated, IsStaff]
    serializer_class = ParcelSerializer


class UserParcelViewSet(ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ParcelSerializer

    def get_queryset(self):
        user = self.request.user
        return Parcel.objects.filter(recipient=user)
