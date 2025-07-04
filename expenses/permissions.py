from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to see or edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to the owner of the object.
        return obj.user == request.user
