from task_app.models import Task, List
from sub_task_app.models import Sub_Task
from django.shortcuts import get_object_or_404


def completed_task(task, task_id):
    task.completed = True
    task.full_clean()
    task.save()
    sub_tasks = Sub_Task.objects.filter(parent_task_id=task_id)
    for sub_task in sub_tasks:
        sub_task.completed = True
        sub_task.full_clean()
        sub_task.save()

def verify_subtasks_complete(parent_task, sub_tasks_list):
    all_done = True
    for sub_task in sub_tasks_list:
        if sub_task.completed == False:
            all_done = False
    if all_done == True:
        parent_task.completed = True
        parent_task.full_clean()
        parent_task.save()
    else:
        parent_task.completed = False
        parent_task.full_clean()
        parent_task.save()

def completed_subtasks(sub_task, task_id):
    parent_task = Task.objects.get(id=task_id)
    sub_task.completed = True
    sub_task.full_clean()
    sub_task.save()
    all_sub_tasks = Sub_Task.objects.filter(parent_task_id=task_id)
    verify_subtasks_complete(parent_task, all_sub_tasks)

def incomplete_subtasks(sub_task, task_id):
    parent_task = Task.objects.get(id=task_id)
    sub_task.completed = False
    sub_task.full_clean()
    sub_task.save()
    all_sub_tasks = Sub_Task.objects.filter(parent_task_id=task_id)
    verify_subtasks_complete(parent_task, all_sub_tasks)