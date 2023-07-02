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

class GetImage(APIView):
    serializer_class = ImageSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, format=None):
        id = request.GET.get(self.lookup_url_kwarg)
        if id != None:
            image = Image.objects.filter(id=id)
            if len(image) > 0:
                data = ImageSerializer(image[0]).data
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Image Not Found': 'Invalid Image Id.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Id paramater not found in request'}, status=status.HTTP_400_BAD_REQUEST)