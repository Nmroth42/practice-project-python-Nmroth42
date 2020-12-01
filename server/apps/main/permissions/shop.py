from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.eats.models import Shop


class ShopPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and 'pk' in view.kwargs and request.user.id is view.get_object().owner_id:
            return True
        if request.user.is_authenticated and request.method == "POST":
            return True
        return False
