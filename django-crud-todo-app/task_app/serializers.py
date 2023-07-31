from rest_framework import serializers
from .models import Task

class Task_Serializer(serializers.ModelSerializer):
    
    parent_list_name = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'task_name', 'parent_list_name', 'completed']

    def get_parent_list_name(self, obj):
        return obj.parent_list.list_name