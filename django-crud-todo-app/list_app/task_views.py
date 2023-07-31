from django.shortcuts import render
from rest_framework.views import APIView, Response
from task_app.models import Task, List
from sub_task_app.models import Sub_Task
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED
from .utilities import get_object_or_404, completed_task
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from task_app.serializers import Task_Serializer
from sub_task_app.serializers import Sub_Task_Serializer

class All_Tasks(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        all_tasks_for_list = Task.objects.filter(parent_list_id=id)
        json_tasks = Task_Serializer(all_tasks_for_list, many=True).data
      
        return Response(json_tasks)

    def post(self, request, id):
        new_task = Task(**request.data)
        new_task.parent_list = get_object_or_404(List, id=id)
        new_task.full_clean()
        new_task.save()
        json_new_task = Task_Serializer(new_task).data

        return Response(json_new_task, status=HTTP_201_CREATED)
    
class A_Task(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id, task_id):
        a_task = get_object_or_404(Task, parent_list_id=id, id=task_id)
        json_task = Task_Serializer(a_task).data
        task_sub_tasks = Sub_Task.objects.filter(parent_task_id=task_id)
        task_sub_tasks_list_json = Sub_Task_Serializer(task_sub_tasks, many=True).data
        json_task['sub_tasks'] = task_sub_tasks_list_json

        return Response(json_task)
    
    def put(self,request, id, task_id):
        a_task = get_object_or_404(Task, parent_list_id=id, id=task_id)
        name = request.data.get('task_name')
        completed = request.data.get('completed')

        if name:
            a_task.task_name = name
            a_task.full_clean()
            a_task.save()
        if completed == True:
            completed_task(a_task, task_id)
        else:
            a_task.completed = False
            a_task.full_clean()
            a_task.save()

        return Response(status=HTTP_204_NO_CONTENT)
    
    def delete(self, request, id, task_id):
        a_task = get_object_or_404(Task, parent_list_id=id, id=task_id)
        a_task.delete()

        return Response(status=HTTP_204_NO_CONTENT)
        