from django.shortcuts import render
from rest_framework import viewsets
from .models import Hero
from .serializers import HeroSerializer
# Create your views here.
# 1. Query the database for all heroes
# 2. Pass that database queryset into the serializer we just created, so that it gets converted into JSON and rendered
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer