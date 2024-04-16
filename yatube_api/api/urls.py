from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


API_VERSION = "v1"


app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"groups", GroupViewSet, basename="group")
router.register(r"follow", FollowViewSet, basename="follow")
router.register(
    r"posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename="comment"
)

urlpatterns = [
    path(f"{API_VERSION}/", include(router.urls)),
    path(
        f"{API_VERSION}/jwt/create/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        f"{API_VERSION}/jwt/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path(
        f"{API_VERSION}/jwt/verify/",
        TokenVerifyView.as_view(),
        name="token_verify"
    ),
]
