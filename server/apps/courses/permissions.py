from rest_framework import permissions

class IsInstructorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or
            request.user.is_authenticated and request.user.role == 'instructor'
        )
