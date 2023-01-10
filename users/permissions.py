from rest_framework import permissions
from .models import User
from rest_framework.views import View
from houses.models import House

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and obj == request.user

class IsHouseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: House) -> bool:
        return request.user.is_authenticated and str(obj[0].user_id) == str(request.user.id)

