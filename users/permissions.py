from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """
    Разрешение для доступа только для активных сотрудников.
    """

    def has_permission(self, request, view):
        # Проверяем, является ли пользователь активным сотрудником
        return request.user.is_authenticated and request.user.is_active
