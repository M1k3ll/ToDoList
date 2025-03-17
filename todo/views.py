from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . models import Todo
from .serializers import TodoSerializer



@api_view(['GET'])
def all_todos(request):
    todos = Todo.objects.order_by('priority').all()
    todo_serializers = TodoSerializer(todos,many=True)
    return Response(todo_serializers.data,status.HTTP_200_OK)



