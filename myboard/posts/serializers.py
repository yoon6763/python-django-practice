from rest_framework import serializers

from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("pk", "post", "text")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text")


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "author", "title", "body", "image", "published_date", "likes", "comments")


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        models = Post
        fields = ("title", "category", "body", "image")
