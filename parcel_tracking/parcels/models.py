import uuid

from django.db import models
from django.core.exceptions import ValidationError

from parcel_tracking.hubs.models import Hub
from parcel_tracking.users.models import User


class ParcelAddress(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street} - {self.city} - {self.state} - {self.zip}"


class ParcelSize(models.Model):
    price = models.IntegerField()
    description = models.TextField(max_length=50)
    max_height = models.IntegerField()
    max_width = models.IntegerField()
    max_length = models.IntegerField()

    def __str__(self):
        return f"{self.description} - {self.price}"


class Parcel(models.Model):

    class StatusParcel(models.TextChoices):
        CREATED = "CREATED"
        AWAITING_DISPATCH = "AWAITING_DISPATCH"
        DISPATCHED = "DISPATCHED"
        IN_TRANSIT = "IN_TRANSIT"
        DELIVERED = "DELIVERED"
        FAILED_DELIVERING = "FAILED_DELIVERING"
        LOST = "LOST"
        DAMAGED = "DAMAGED"
        CANCELLED = "CANCELLED"

    content_description = models.TextField(max_length=100, blank=True)
    content_value = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    size = models.ForeignKey(ParcelSize, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=100, choices=StatusParcel, default=StatusParcel.CREATED
    )
    address = models.ForeignKey(ParcelAddress, on_delete=models.CASCADE)
    courier = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="courier_name",
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="recipient_name",
    )
    hub = models.ForeignKey(
        Hub, on_delete=models.CASCADE, blank=True, null=True, related_name="parcels_hub"
    )

    def __str__(self):
        return f"{self.content_description}"

    def clean(self):
        if self.courier and self.courier.role.name != "courier":
            raise ValidationError("The assigned user must have the role courier")


class DamagedParcel(models.Model):
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    parcel = models.ForeignKey(
        Parcel, on_delete=models.CASCADE, related_name="damaged_records"
    )
