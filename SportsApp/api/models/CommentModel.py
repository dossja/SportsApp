from django.db import models
from django.contrib.auth.models import User
from .PostModel import Post

# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    description = models.CharField(max_length=1000, null=False)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name="comments", null=True)

    class Meta:
        pass