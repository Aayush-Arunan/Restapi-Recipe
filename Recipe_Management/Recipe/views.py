from django.shortcuts import render
from Recipe.models import Cuisine
from Recipe.serializers import CuisineSerializer
from Recipe.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated






class Recipes(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Cuisine.objects.all()
    serializer_class = CuisineSerializer


class CreateUser(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer









