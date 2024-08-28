from factory.django import DjangoModelFactory
from ..models import Hub
from factory import Faker, SubFactory


class HubFactory(DjangoModelFactory):

    name = Faker("word")
    address = Faker("word")
    province = Faker("word")
    city = Faker("word")
    zipcode = Faker("word")

    class Meta:
        model = Hub
