from rest_framework import serializers
from .models import List
from task_app.serializers import Task_Serializer

class List_Serializer(serializers.ModelSerializer):

    tasks = Task_Serializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = ['id', 'list_name', 'tasks']

   

    