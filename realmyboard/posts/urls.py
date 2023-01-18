from django.urls import path

from posts.views import PostView, like_post

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>/', PostView.as_view()),
    path('like/<int:pk>/', like_post, name='like_post'),
]
