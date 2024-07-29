from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import generics

from .models import Hub
from .serializers import HubSerializer


# Create your views here.
class HubListCreateView(generics.ListCreateAPIView):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer

class HubRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer
    lookup_field = 'pk'

