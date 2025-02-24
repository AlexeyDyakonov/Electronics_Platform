from rest_framework import permissions


class IsActiveStaff(permissions.BasePermission):
    """Проверка активности сотрудника"""

    def has_permission(self, request, view):
        if request.user.is_active and request.user.is_staff:
            return True
        return False
