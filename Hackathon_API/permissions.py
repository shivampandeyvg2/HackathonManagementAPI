from rest_framework.permissions import BasePermission

class IsHackathonCreator(BasePermission):
    def __init__(self, allowed_groups=None):
        self.allowed_groups = allowed_groups or []

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        result=  request.user.groups.filter(name='hackathon_masters').exists()
        return  result