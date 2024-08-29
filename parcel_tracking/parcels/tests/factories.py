from factory.django import DjangoModelFactory

from parcel_tracking.parcels.models import ParcelSize, ParcelAddress, Parcel
from factory import Faker, post_generation, SubFactory

from parcel_tracking.users.tests.factories import UserFactory


class ParcelSizeFactory(DjangoModelFactory):

    price = Faker("random_int", min=1, max=20)
    description = Faker("word")
    max_height = Faker("random_int", min=1, max=20)
    max_length = Faker("random_int", min=1, max=20)
    max_width = Faker("random_int", min=1, max=20)

    class Meta:
        model = ParcelSize


class ParcelAddressFactory(DjangoModelFactory):

    name = Faker("word")
    surname = Faker("word")
    street = Faker("word")
    city = Faker("word")
    country = Faker("word")
    state = Faker("word")
    zip = Faker("word")

    class Meta:
        model = ParcelAddress


class ParcelFactory(DjangoModelFactory):

    content_description = Faker("sentence")
    content_value = Faker("random_int", min=10, max=1000)
    weight = Faker("random_int", min=1, max=20)
    height = Faker("random_int", min=10, max=100)
    width = Faker("random_int", min=10, max=100)
    length = Faker("random_int", min=10, max=100)
    size = SubFactory(ParcelSizeFactory)
    status = Parcel.StatusParcel.CREATED  # Default status
    address = SubFactory(ParcelAddressFactory)
    courier = SubFactory(UserFactory)
    recipient = SubFactory(UserFactory)

    class Meta:
        model = Parcel
