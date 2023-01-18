from django.urls import path

from posts.views import PostView, like_post, CommentView, CommentPostView

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>/', PostView.as_view()),
    path('posts/like/<int:pk>/', like_post, name='like_post'),
    path('comments/', CommentView.as_view()),
    path('comments/<int:pk>/', CommentView.as_view()),
    path('comments/post/', CommentPostView.as_view()),
]
