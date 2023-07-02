from django.db import models
from django.contrib.auth.models import User
from .ImageModel import Image

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000, null=True)
    images = models.ManyToManyField(Image)

    class Meta:
        pass