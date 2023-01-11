from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Comments



class isCommentOwner(BasePermission):
    def has_object_permission(self, request, view, comment: Comments):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_authenticated and comment.user_id == request.user.id
