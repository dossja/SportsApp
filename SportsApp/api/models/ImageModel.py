from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="image")
    img = models.ImageField(upload_to='images')

    class Meta:
        pass