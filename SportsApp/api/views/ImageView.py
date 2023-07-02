from django.shortcuts import render
from rest_framework import generics, status
from ..serializers.ImageSerializer import ImageSerializer
from ..models.ImageModel import Image
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

class ImageView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer