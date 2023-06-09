from django.shortcuts import render
from ..service_app.models import Cars, CarQueue
from .serializer import CarsSerializer, CarQueueSerializer
from django.http import Http404
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class CarApiVeiw(APIView):
    """
    List all snippets, or create a new snippet.
    """
    
    def get_object(self, pk):
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CarsSerializer(snippet)
        return Response(serializer.data)
    
class CarQueueApiVeiw(APIView):
    """
    List all snippets, or create a new snippet.
    """
    
    def get_object(self, pk):
        try:
            return CarQueue.objects.get(pk=pk)
        except CarQueue.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CarQueueSerializer(snippet)
        return Response(serializer.data)