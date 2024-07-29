from django.urls import path

from . import views

urlpatterns = [
    path("hub/", views.HubListCreateView.as_view(), name="hub"),
    path("hub/<int:pk>/", views.HubRetrieveUpdateDestroyView.as_view(), name="hub-detail"),
]