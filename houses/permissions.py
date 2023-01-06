from rest_framework.permissions import BasePermission
from rest_framework.views import Request, View
from houses.models import House

class isHouseOwner(BasePermission):
    def has_object_permission(self, request, view, house: House):
        return house.user_id == request.user.id