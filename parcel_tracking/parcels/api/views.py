
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from parcel_tracking.parcels.api.serializers import ParcelAddressSerializer, ParcelSizeSerializer, ParcelSerializer
from parcel_tracking.parcels.models import Parcel, ParcelAddress, ParcelSize
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

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



