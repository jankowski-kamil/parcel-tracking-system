import pytest
from .factories import ParcelSizeFactory, ParcelAddressFactory, ParcelFactory
from django.urls import reverse


class TestHubsViewSet:

    @pytest.mark.django_db()
    def test_list_parce_size(self, api_client, user):
        api_client.force_authenticate(user=user)
        parcel_sizes = ParcelSizeFactory.create_batch(10)
        url = reverse("parcels:parcel-size-list")
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) == len(parcel_sizes)

    @pytest.mark.django_db()
    def test_create_parcel_size(self, api_client, user):
        api_client.force_authenticate(user=user)
        payload = {
            "price": 12,
            "description": "gadget",
            "max_height": 15,
            "max_length": 8,
            "max_width": 10,
        }
        url = reverse("parcels:parcel-size-list")
        response = api_client.post(url, payload)
        assert response.status_code == 201

    @pytest.mark.django_db()
    def test_detail_parcel_size(self, api_client, user):
        api_client.force_authenticate(user=user)
        parcel_sizes = ParcelSizeFactory.create_batch(10)
        url = reverse("parcels:parcel-size-detail", kwargs={"pk": parcel_sizes[0].id})
        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db()
    def test_update_parcel_size(self, api_client, user):
        api_client.force_authenticate(user=user)
        parcel_sizes = ParcelSizeFactory.create_batch(10)
        payload = {
            "price": 12,
            "description": "gadget",
            "max_height": 15,
            "max_length": 8,
            "max_width": 10,
        }
        url = reverse("parcels:parcel-size-detail", kwargs={"pk": parcel_sizes[0].id})
        response = api_client.patch(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db()
    def test_delete_parcel_size(self, api_client, user):
        api_client.force_authenticate(user=user)
        parcel_sizes = ParcelSizeFactory.create_batch(10)
        url = reverse("parcels:parcel-size-detail", kwargs={"pk": parcel_sizes[0].id})
        response = api_client.delete(url)
        assert response.status_code == 204

    @pytest.mark.django_db()
    def test_list_parcel_addresses(self, api_client, user):
        api_client.force_authenticate(user=user)
        parcel_addresses = ParcelAddressFactory.create_batch(10)
        url = reverse("parcels:parcel-address-list")
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) == len(parcel_addresses)

    @pytest.mark.django_db()
    def test_detail_parcel_address(self, api_client, user):
        api_client.force_authenticate(user=user)
        parcel_addresses = ParcelAddressFactory.create_batch(10)
        url = reverse(
            "parcels:parcel-address-detail", kwargs={"pk": parcel_addresses[0].id}
        )
        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db()
    def test_create_parcel_address(self, api_client, user):
        api_client.force_authenticate(user=user)
        payload = {
            "name": "John",
            "surname": "Doe",
            "street": "123 Elm Street",
            "city": "Springfield",
            "country": "USA",
            "state": "Illinois",
            "zip": "62704",
        }
        url = reverse("parcels:parcel-address-list")
        response = api_client.post(url, payload)
        assert response.status_code == 201

    @pytest.mark.django_db()
    def test_update_parcel_address(self, api_client, user):
        api_client.force_authenticate(user=user)
        parcel_addresses = ParcelAddressFactory.create_batch(10)
        payload = {
            "name": "John",
            "surname": "Doe",
            "street": "123 Elm Street",
            "city": "Springfield",
            "country": "USA",
            "state": "Illinois",
            "zip": "62704",
        }
        url = reverse(
            "parcels:parcel-address-detail", kwargs={"pk": parcel_addresses[0].id}
        )
        response = api_client.patch(url, payload)
        assert response.status_code == 200

    @pytest.mark.django_db()
    def test_delete_parcel_address(self, api_client, user):
        api_client.force_authenticate(user=user)
        parcel_addresses = ParcelAddressFactory.create_batch(10)
        url = reverse(
            "parcels:parcel-address-detail", kwargs={"pk": parcel_addresses[0].id}
        )
        response = api_client.delete(url)
        assert response.status_code == 204

    @pytest.mark.django_db()
    def test_user_parcel_list(self, api_client, user):
        api_client.force_authenticate(user=user)
        ParcelAddressFactory.create_batch(10)
        url = reverse("parcels:parcel-user-list")
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 0


