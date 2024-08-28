from django.contrib import admin
from .models import Hub

@admin.register(Hub)
class HubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'city')
    search_fields = ('id','name')
