from rest_framework import serializers
from ..models.PostModel import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'description', 'images')