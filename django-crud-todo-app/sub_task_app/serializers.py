from rest_framework import serializers
from .models import Sub_Task

class Sub_Task_Serializer(serializers.ModelSerializer):
    
    parent_task_name = serializers.SerializerMethodField()

    class Meta:
        model = Sub_Task
        fields = ['id', 'sub_task_name', 'parent_task_name', 'completed']

    def get_parent_task_name(self, obj):
        return obj.parent_task.task_name