
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . models import Todo
from .serializers import TodoSerializer,UserSerializer
from rest_framework import viewsets,generics
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
User = get_user_model()

#apiregion
@api_view(['GET'])
def all_todos(request):
    todos = Todo.objects.order_by('priority').all()
    todo_serializers = TodoSerializer(todos,many=True)
    return Response(todo_serializers.data,status.HTTP_200_OK)

#endregion

class TodoViewSetApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    # permission_classes = [IsAuthenticated]

#region user

class UsersGenericApiview(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



#endregion