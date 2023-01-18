from django.urls import path

from comments.views import CommentView, CommentPostView, like_comment

urlpatterns = [
    path('', CommentView.as_view()),
    path('<int:pk>/', CommentView.as_view()),
    path('post/', CommentPostView.as_view()),
    path('like/<int:pk>/', like_comment, name='like_post')
]
