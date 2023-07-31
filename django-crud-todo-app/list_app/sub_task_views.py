from django.shortcuts import render
from rest_framework.views import APIView, Response
from task_app.models import Task, List
from sub_task_app.models import Sub_Task
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED
from .utilities import get_object_or_404, completed_subtasks, incomplete_subtasks
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from sub_task_app.serializers import Sub_Task_Serializer

class All_Sub_Tasks(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id, task_id):
        all_sub_tasks_for_task = Sub_Task.objects.filter(parent_task_id=task_id)   
        json_sub_tasks = Sub_Task_Serializer(all_sub_tasks_for_task, many=True)
        
        return Response(json_sub_tasks.data)
    
    def post(self, request, id, task_id):
        new_sub_task = Sub_Task(**request.data)
        new_sub_task.parent_task = get_object_or_404(Task, parent_list_id=id, id=task_id)
        new_sub_task.full_clean()
        new_sub_task.save()
        json_new_sub_task = Sub_Task_Serializer(new_sub_task).data

        parent_task = Task.objects.get(id=task_id)
        parent_task.completed = False
        parent_task.full_clean()
        parent_task.save()

        return Response(json_new_sub_task, status=HTTP_201_CREATED)

class A_Sub_Task(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id, task_id, subtask_id):
        a_sub_task = get_object_or_404(Sub_Task, parent_task_id=task_id, id=subtask_id)
        json_sub_task = Sub_Task_Serializer(a_sub_task).data

        return Response(json_sub_task)
    
    def put(self, request, id, task_id, subtask_id):
        a_sub_task = get_object_or_404(Sub_Task, parent_task_id=task_id, id=subtask_id)
        name = request.data.get('sub_task_name')
        completed = request.data.get('completed')

        if name:
            a_sub_task.sub_task_name = name
            a_sub_task.full_clean()
            a_sub_task.save()
        if completed == True:
            completed_subtasks(a_sub_task, task_id)
        elif completed == False:
            incomplete_subtasks(a_sub_task, task_id)

        return Response(status=HTTP_204_NO_CONTENT)
    
    def delete(self, request, id, task_id, subtask_id):
        a_sub_task = get_object_or_404(Sub_Task, parent_task_id=task_id, id=subtask_id)
        a_sub_task.delete()

        return Response(status=HTTP_204_NO_CONTENT)