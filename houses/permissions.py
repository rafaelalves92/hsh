from rest_framework import permissions
from .models import House, LocationHouse
from rest_framework.views import View


class IsHouseOwnerOrRenter(permissions.BasePermission):
    def has_object_permission(self, request, view: View, object: House) -> bool:
        return request.user.is_authenticated and object.user_id != request.user.id
