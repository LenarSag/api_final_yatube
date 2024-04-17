from rest_framework import permissions


class CustomObjectPermissions(permissions.BasePermission):
    """
    Пользовательские разрешения на уровне объекта для представлений.
    Этот класс разрешений предоставляет настраиваемые разрешения
    на основе типа запроса и автора объекта.
    """

    def has_permission(self, request, view):
        """
        Проверка на то, что запрос GET, иначе проверка на аутентификацию.
        """
        if view.action in ["retrieve", "list"]:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        При запросе конкретного обьекта, если запрос на изменение/удаление,
        то проверяем, что автор запроса == автор обьекта. В отсальных случаях
        возвращаем True.
        """
        if view.action in ["update", "partial_update", "destroy"]:
            return obj.author == request.user
        return True

    # проверить сейв методы head, options
