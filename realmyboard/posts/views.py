from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostSerializer, PostCreateSerializer


# Create your views here.
class PostView(APIView):
    # def post(self, request):
    #     serializer = PostCreateSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save(author=self.request.user)
    #         serializer.save()
    #         return Response(serializer, serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=self.request.user)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def like_post(request, pk):
    # 토큰이 없을 때
    if not request.user.is_authenticated:
        return Response({"message": "Token is needed"}, status=status.HTTP_401_UNAUTHORIZED)

    post = get_object_or_404(Post, pk=pk)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    return Response({"is_liked": is_liked}, status=status.HTTP_200_OK)
