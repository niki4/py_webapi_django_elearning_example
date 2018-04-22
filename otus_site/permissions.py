from rest_framework import permissions


class IsAccountAdminOrReadOnly(permissions.BasePermission):
    """
    Read-only requests are allowed for any users (both authorized and anonymous).
    Write/Delete requests are allowed only to authorized Admin.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_staff
        )
