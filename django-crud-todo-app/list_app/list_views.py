from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import List
from task_app.models import Task
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import List_Serializer
from task_app.serializers import Task_Serializer

# Create your views here.
class All_Lists(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_lists = List.objects.all()
        json_lists = List_Serializer(all_lists, many=True).data

        return Response(json_lists)
    
    def post(self, request):
        new_list = List(**request.data)
        new_list.full_clean()
        new_list.save()
        json_new_list = List_Serializer(new_list).data
        return Response(json_new_list, status=HTTP_201_CREATED)
    
class A_List(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        a_list = get_object_or_404(List, id=id)
        json_list = List_Serializer(a_list).data
        tasks = Task.objects.filter(parent_list_id=id)
        tasks = Task_Serializer(tasks, many=True).data
        json_list['tasks'] = tasks

        return Response(json_list)
    
    def put(self, request, id):
        a_list = get_object_or_404(List, id=id)
        new_name = request.data.get('list_name')
        if new_name:
            a_list.list_name = new_name
            a_list.full_clean()
            a_list.save()

        return Response(status=HTTP_204_NO_CONTENT)
    
    def delete(self, request, id):
        a_list = get_object_or_404(List, id=id)
        a_list.delete()

        return Response(status=HTTP_204_NO_CONTENT)