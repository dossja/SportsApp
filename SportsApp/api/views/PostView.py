from django.shortcuts import render
from rest_framework import generics, status
from ..serializers.PostSerializer import PostSerializer
from ..models.PostModel import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer