from rest_framework import serializers

from posts.models import Post
from users.serializers import UserSerializer


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'title', 'subject', 'content']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # nested Serializer, foreign key 로 연결된 테이블 정보까지 가져옴

    class Meta:
        model = Post
        fields = ['pk', 'author', 'title', 'subject', 'content', 'likes', 'published_date']
