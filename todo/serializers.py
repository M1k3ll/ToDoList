from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model


user = get_user_model()

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','title','content','priority','is_done','user']
        



class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)
    class Meta:
        model = user
        fields = '__all__'
        