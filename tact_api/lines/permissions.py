from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        """
        allows read permission to any request.
        i.e. GET, HEAD and OPTIONS requests are always allowed.
        I.e. PUT requests are only allowed to object owner.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
