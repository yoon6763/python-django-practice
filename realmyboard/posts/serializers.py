from rest_framework import serializers

from posts.models import Post, Comment
from users.serializers import UserSerializer


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'post', 'content']


class CommentSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    author = UserSerializer(read_only=True)  # nested Serializer, foreign key 로 연결된 테이블 정보까지 가져옴

    class Meta:
        model = Comment
        fields = ['pk', 'author', 'post', 'content', 'likes', 'published_date']


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'title', 'subject', 'content']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # nested Serializer, foreign key 로 연결된 테이블 정보까지 가져옴

    class Meta:
        model = Post
        fields = ['pk', 'author', 'title', 'subject', 'content', 'likes', 'published_date']
