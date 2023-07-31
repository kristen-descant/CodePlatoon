from django.urls import path
from .list_views import All_Lists, A_List
from .task_views import All_Tasks, A_Task
from .sub_task_views import All_Sub_Tasks, A_Sub_Task

urlpatterns = [
    path('', All_Lists.as_view(), name='all_lists'),
    path('<int:id>/', A_List.as_view(), name='a_list'),
    path('<int:id>/tasks/', All_Tasks.as_view(), name='all_tasks'),
    path('<int:id>/tasks/<int:task_id>/', A_Task.as_view(), name='a_task'),
    path('<int:id>/tasks/<int:task_id>/subtasks/', All_Sub_Tasks.as_view(), name='all_sub_tasks'),
    path('<int:id>/tasks/<int:task_id>/subtasks/<int:subtask_id>/', A_Sub_Task.as_view(), name='a_sub_task'),
]