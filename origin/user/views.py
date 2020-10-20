# Django impors:
from django.shortcuts import render
from django.contrib.auth.models import User

# Rest framework imports:
from rest_framework import status, viewsets

# Serializer imports:
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer