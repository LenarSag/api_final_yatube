from rest_framework import permissions


class CustomObjectPermissions(permissions.BasePermission):
    """
    Этот класс разрешений предоставляет настраиваемые разрешения
    на основе типа запроса и проверки авторства объекта.
    """

    def has_permission(self, request, view):
        """
        Проверка на то, что запрос GET, HEAD или OPTIONS,
        иначе проверка на аутентификацию.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        При запросе конкретного обьекта, если запрос на изменение/удаление,
        то проверяем, что автор запроса == автор обьекта. В остальных случаях
        возвращаем True.
        """
        if request.method not in permissions.SAFE_METHODS:
            return obj.author == request.user
        return True
