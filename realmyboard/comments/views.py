from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from comments.models import Comment
from comments.serializers import CommentCreateSerializer, CommentSerializer


# Create your views here.

class CommentView(APIView):

    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data)

        if not request.user.is_authenticated:
            return Response({'message': "Token needed"}, status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            serializer.save(author=self.request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        serializer = CommentSerializer(get_object_or_404(Comment, pk=pk))
        return Response(serializer.data)

    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)

        if not request.user.is_authenticated:
            return Response({'message': "Token needed"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not request.user.is_authenticated:
            return Response({'message': "Token needed"}, status=status.HTTP_401_UNAUTHORIZED)
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentPostView(APIView):
    def get(self, request):
        pk = request.GET.get("post_pk")
        comments = Comment.objects.filter(post=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def like_comment(request, pk):
    # 토큰이 없을 때
    if not request.user.is_authenticated:
        return Response({"message": "Token is needed"}, status=status.HTTP_401_UNAUTHORIZED)

    comment = get_object_or_404(Comment, pk=pk)

    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
        is_liked = False
    else:
        comment.likes.add(request.user)
        is_liked = True

    return Response({"is_liked": is_liked}, status=status.HTTP_200_OK)

