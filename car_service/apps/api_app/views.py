from typing import Any
from django.shortcuts import render
from ..service_app.models import Cars, CarQueue, RepairHistory, CustomerProfile
from .serializer import CarsSerializer, CarQueueSerializer, RepairHistorySerializer,\
    CustomerSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class ApiFunctions(APIView):
    def get_object(self, pk):
        try:
            return self.object.objects.get(pk=pk)
        except self.object.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = self.serializer(snippet)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = self.serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarApiVeiw(ApiFunctions):

    def __init__(self):
        self.serializer = CarsSerializer
        self.object = Cars
    
    
    
class CustomerApiView(ApiFunctions):
    def __init__(self):
        self.serializer = CustomerSerializer
        self.object = CustomerProfile

    
class CarQueueApiVeiw(ApiFunctions):
    def __init__(self):
        self.serializer = CarQueueSerializer
        self.object = CarQueue

    
    # def get_object(self, pk):
    #     try:
    #         return CarQueue.objects.get(pk=pk)
    #     except CarQueue.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = CarQueueSerializer(snippet)
    #     return Response(serializer.data)
    
    
class InvoiceApiView(ApiFunctions):
    def __init__(self):
        self.serializer = RepairHistorySerializer
        self.object = RepairHistory
    # def get_object(self, pk):
    #     try:
    #         return RepairHistory.objects.get(pk=pk)
    #     except RepairHistory.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = RepairHistorySerializer(snippet)
    #     return Response(serializer.data)