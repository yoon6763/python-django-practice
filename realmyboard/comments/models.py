from django.db import models
from django.utils import timezone

from posts.models import Post
from users.models import User


# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='like_comments', blank=True)
    published_date = models.DateTimeField(default=timezone.now)
