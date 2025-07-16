from django.shortcuts import render
from rest_framework import viewsets
from .models import data
from .serializers import dataSerializers



# Create your views here.


class dataViewset(viewsets.ModelViewSet):
    queryset = data.objects.all()
    serializer_class =dataSerializers
