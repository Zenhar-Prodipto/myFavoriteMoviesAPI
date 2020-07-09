from django.shortcuts import render
from .models import Movie
from .serializers import serializerClass
from rest_framework import viewsets

# Create your views here.
class viewClass(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = serializerClass