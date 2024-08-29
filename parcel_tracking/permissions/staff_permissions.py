from rest_framework.permissions import BasePermission
from rest_framework import permissions

from parcel_tracking.users.models import User


class IsStaff(BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        return User.objects.get(pk=request.user.id).role.name != 'client'
