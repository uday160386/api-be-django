from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Medicines
from .serializers import MedicineSerializer


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicines.objects.all()
    serializer_class = MedicineSerializer

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        rating = Medicines.objects.create(title=request.title, description=request.description, qty=request.qty)
        serializer = MedicineSerializer(rating, many=False)
        response = {'message': 'Order created', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)
