from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializers
from .models import Hero

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializers

# Create your views here.
