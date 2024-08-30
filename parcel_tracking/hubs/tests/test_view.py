import pytest
from .factories import HubFactory
from django.urls import reverse


class TestHubsViewSet:

    @pytest.mark.django_db()
    def test_list_hubs(self, api_client, user):
        api_client.force_authenticate(user=user)
        hubs = HubFactory.create_batch(10)
        url = reverse("hubs:hubs-list")
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) == len(hubs)

    @pytest.mark.django_db()
    def test_detail_hub(self, api_client, user):
        api_client.force_authenticate(user=user)
        hubs = HubFactory.create_batch(10)
        url = reverse("hubs:hubs-detail", kwargs={"pk": hubs[0].pk})
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data["name"] == hubs[0].name

    @pytest.mark.django_db()
    def test_detail_hub_not_found(self, api_client, user):
        api_client.force_authenticate(user=user)
        url = reverse("hubs:hubs-detail", kwargs={"pk": 321})
        response = api_client.get(url)
        assert response.status_code == 404

    @pytest.mark.django_db()
    def test_create(self, api_client, user):
        api_client.force_authenticate(user=user)
        url = reverse("hubs:hubs-list")
        payload = {
            "name": "John Doe",
            "address": "123 Main Street",
            "province": "Mazowieckie",
            "city": "Warsaw",
            "zipcode": "00-001",
        }
        response = api_client.post(url, payload)
        assert response.status_code == 201
        assert response.data["name"] == payload["name"]

    @pytest.mark.django_db()
    def test_search(self, api_client, user):
        api_client.force_authenticate(user=user)
        hubs = HubFactory.create_batch(10)
        base_url = reverse("hubs:hubs-list")
        search_term = hubs[0].name
        url = f"{base_url}?search={search_term}"
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 1

    @pytest.mark.django_db()
    def test_ordering_by_name(self, api_client, user):
        api_client.force_authenticate(user=user)
        hubs = HubFactory.create_batch(10)
        sorted_hubs = sorted(hubs, key=lambda hub: hub.name)
        base_url = reverse("hubs:hubs-list")
        url = f"{base_url}?ordering=name"
        response = api_client.get(url)
        assert response.status_code == 200
        assert sorted_hubs[0].name == response.data[0]["name"]

