from django.contrib import admin

from parcel_tracking.parcels.models import (
    Parcel,
    ParcelSize,
    ParcelAddress,
    DamagedParcel,
)


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content_description",
        "content_value",
        "weight",
        "height",
        "length",
        "size",
        "status",
    )
    search_fields = ("id", "content_description")
    list_filter = ("status",)


@admin.register(ParcelSize)
class ParcelSizeAdmin(admin.ModelAdmin):
    list_display = ("id", "price", "description")
    search_fields = ("id", "description")
    list_filter = ("id", "price", "description")


@admin.register(ParcelAddress)
class ParcelAddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "surname",
        "street",
        "city",
        "state",
        "zip",
        "country",
    )
    search_fields = ("id", "name", "surname")
    list_filter = ("id", "name", "surname")


@admin.register(DamagedParcel)
class DamagedParcelRecordAdmin(admin.ModelAdmin):
    list_display = ("parcel", "description", "created_at")
