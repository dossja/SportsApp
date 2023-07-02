from rest_framework import serializers
from ..models.CommentModel import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'description', 'post')