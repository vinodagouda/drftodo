from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from todo_api.models import ToDo
from todo_api.serializers import ToDoSerializer

# Create your views here.

class ToDoViewSet(viewsets.ModelViewSet):

	authentication_classes = [JWTAuthentication, TokenAuthentication]
	permission_classes = [IsAuthenticated]

	queryset = ToDo.objects.all()
	serializer_class = ToDoSerializer