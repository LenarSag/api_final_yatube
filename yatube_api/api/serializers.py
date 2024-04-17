from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers


from posts.models import Post, Group, Comment, Follow


User = get_user_model()


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    def validate(self, attrs):
        following_username = attrs.get("following").username
        user_username = self.context["request"].user.username
        if following_username == user_username:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя!"
            )
        return attrs

    class Meta:
        model = Follow
        exclude = ("id",)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=("user", "following")
            )
        ]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("post",)
