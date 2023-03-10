from rest_framework import serializers

from posts.models import Post, Comment
from users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "author", "post", "text")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text")


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # nested Serializer
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "author", "title", "body", "image", "published_date", "likes", "comments")


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        models = Post
        fields = ("title", "category", "body", "image")
