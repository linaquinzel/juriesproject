from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import User
from .serializer import UserSerializer

# Create your views here.
class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer