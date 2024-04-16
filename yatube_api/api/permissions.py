from rest_framework import permissions

from posts.models import Post


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
        )


class BasePermissionWithSafeMethods(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )


class AuthorOrReadOnly(BasePermissionWithSafeMethods):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class PostExistsAndAuthorOrReadOnly(BasePermissionWithSafeMethods):
    def has_object_permission(self, request, view, obj):
        post = Post.objects.filter(pk=view.kwargs.get("post_id")).first()
        if post is None:
            return False
        return obj.author == request.user
