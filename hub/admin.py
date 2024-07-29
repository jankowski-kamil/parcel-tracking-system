from django.contrib import admin
from .models import Hub

# Register your models here.
@admin.register(Hub)
class HubAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "city", "postal_code", 'created_at']


