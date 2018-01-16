from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Otherwise users have read only access to non-owned objects.
    """

    def has_object_permission(self, request, view, obj):
        """
        i.e. GET, HEAD and OPTIONS requests are allowed with all objects.
        I.e. PUT, DELETE requests are only allowed to object owners.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
