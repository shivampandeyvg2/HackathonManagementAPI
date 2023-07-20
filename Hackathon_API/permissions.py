from rest_framework.permissions import BasePermission

class IsInAllowedGroups(BasePermission):
    def __init__(self, allowed_groups=None):
        self.allowed_groups = allowed_groups or []

    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=self.allowed_groups).exists()