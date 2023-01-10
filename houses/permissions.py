from rest_framework.permissions import BasePermission
from .models import House


class IsHouseOwnerOrRenter(BasePermission):
    def has_object_permission(self, request, view, house: House) -> bool:
        return request.user.is_authenticated and house.user_id != request.user.id


class isHouseOwner(BasePermission):
    def has_object_permission(self, request, view, house: House):
        return request.user.is_authenticated and house.user_id == request.user.id
