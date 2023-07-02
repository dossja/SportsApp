from django.shortcuts import render
from rest_framework import generics, status
from ..serializers.CommentSerializer import CommentSerializer
from ..models.CommentModel import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

class CommentView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer