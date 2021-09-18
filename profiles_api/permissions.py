from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """Alow user to edit there own profile """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id


class UpdateOwnStatus (permissions.BasePermission):
    """Allow user to update"""

    def has_object_permission(self, request, view, obj):
        """check right user to update"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id