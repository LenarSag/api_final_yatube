from rest_framework import permissions
from rest_framework.exceptions import NotFound

from posts.models import Post


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
        )


class AuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class PostExistsAndAuthorOrReadOnly(AuthorOrReadOnly):
    def has_object_permission(self, request, view, obj):
        post = Post.objects.filter(pk=view.kwargs.get("post_id")).first()
        if post is None:
            raise NotFound
        return super().has_object_permission(request, view, obj)
