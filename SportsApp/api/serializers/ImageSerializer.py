from rest_framework import serializers
from ..models.ImageModel import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'author', 'img')