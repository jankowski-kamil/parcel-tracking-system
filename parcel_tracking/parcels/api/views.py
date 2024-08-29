from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from parcel_tracking.parcels.api.serializers import (
    ParcelAddressSerializer,
    ParcelSizeSerializer,
    ParcelSerializer,
    ParcelDamageSerializer,
)
from parcel_tracking.parcels.models import (
    Parcel,
    ParcelAddress,
    ParcelSize,
    DamagedParcel,
)

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

    @action(detail=True, methods=["POST"])
    def change_to_damaged_status(self, request, pk=None):
        parcel = get_object_or_404(Parcel, pk=pk)
        serializer = ParcelDamageSerializer(data=request.data)
        if serializer.is_valid():
            parcel.status = Parcel.StatusParcel.DAMAGED
            parcel.save()
            DamagedParcel.objects.create(
                parcel=parcel, description=serializer.validated_data["description"]
            )
            return Response(f"Status has been changed", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserParcelViewSet(ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ParcelSerializer

    def get_queryset(self):
        user = self.request.user
        return Parcel.objects.filter(recipient=user)
