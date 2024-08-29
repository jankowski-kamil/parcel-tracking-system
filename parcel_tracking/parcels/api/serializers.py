from rest_framework import serializers
from parcel_tracking.parcels.models import (
    ParcelAddress,
    ParcelSize,
    Parcel,
    DamagedParcel,
)


class ParcelAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelAddress
        fields = ["id", "name", "surname", "street", "city", "country", "state", "zip"]


class ParcelSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParcelSize
        fields = ["id", "price", "description", "max_height", "max_width", "max_length"]


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = "__all__"

    def validate_courier(self, value):
        if value and value.role.name != "courier":
            raise serializers.ValidationError(
                "The assigned user must have the role 'courier'."
            )
        return value


class ParcelDamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DamagedParcel
        fields = ("description",)
