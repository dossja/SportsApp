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


class GetPost(APIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, format=None):
        id = request.GET.get(self.lookup_url_kwarg)
        if id != None:
            post = Post.objects.filter(id=id)
            if len(post) > 0:
                data = PostSerializer(post[0]).data
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Post Not Found': 'Invalid Post Id.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Id paramater not found in request'}, status=status.HTTP_400_BAD_REQUEST)