from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer

from .models import Hero


class HeroModelSerializer(ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class HeroViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = HeroModelSerializer
    queryset = Hero.objects.all()
