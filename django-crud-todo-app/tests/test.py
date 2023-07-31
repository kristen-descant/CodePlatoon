from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ValidationError
from list_app.models import List
from task_app.models import Task
from sub_task_app.models import Sub_Task
from tests.answers import all_lists, all_sub_tasks, all_tasks
import json

class List_Test(TestCase):

    def test_01_create_list_instance(self):
        new_list = List(list_name='My Test List')
        try:
            new_list.full_clean()
            self.assertIsNotNone(new_list)
        except ValidationError as e:
            self.fail()
    
    def test_02_create_list_with_too_many_characters(self):
        new_list = List(list_name='This list name is going to exceed the character limit')
        char_count = len(new_list.list_name)
        try:
            new_list.full_clean()
            self.fail()
        except ValidationError as e:
            self.assertTrue(f'Ensure this value has at most 30 characters (it has {char_count}).' in e.message_dict['list_name'])

class Task_Test(TestCase):

    def test_03_create_task_instance(self):
        parent_list = List(list_name='parent_list')
        parent_list.full_clean()
        parent_list.save()
        new_task = Task(task_name='My Test Task', parent_list_id=parent_list.id)
        try:
            new_task.full_clean()
            self.assertIsNotNone(new_task)
        except ValidationError as e:
            self.fail()
    
    def test_04_create_task_with_too_many_characters(self):
        parent_list = List(list_name='parent_list')
        parent_list.full_clean()
        parent_list.save()
        new_task = Task(task_name='This task name is going to exceed the character limit', parent_list_id=parent_list.id)
        char_count = len(new_task.task_name)
        try:
            new_task.full_clean()
            self.fail()
        except ValidationError as e:
            self.assertTrue(f'Ensure this value has at most 30 characters (it has {char_count}).' in e.message_dict['task_name'])

class Sub_Task_Test(TestCase):

    def test_05_create_sub_task_instance(self):
        parent_list = List(list_name='parent_list')
        parent_list.full_clean()
        parent_list.save()
        parent_task = Task(task_name='parent_task', parent_list_id=parent_list.id)
        parent_task.full_clean()
        parent_task.save()
        new_sub_task = Sub_Task(sub_task_name='My Test Sub Task', parent_task_id=parent_task.id)
        try:
            new_sub_task.full_clean()
            self.assertIsNotNone(new_sub_task)
        except ValidationError as e:
            self.fail()

    def test_06_create_sub_task_with_too_many_characters(self):
        parent_list = List(list_name='parent_list')
        parent_list.full_clean()
        parent_list.save()
        parent_task = Task(task_name='parent_task', parent_list_id=parent_list.id)
        parent_task.full_clean()
        parent_task.save()
        new_sub_task = Sub_Task(sub_task_name='This task name is going to exceed the character limit', parent_task_id=parent_task.id)
        char_count = len(new_sub_task.sub_task_name)
        try:
            new_sub_task.full_clean()
            self.fail()
        except ValidationError as e:
            self.assertTrue(f'Ensure this value has at most 30 characters (it has {char_count}).' in e.message_dict['sub_task_name'])

class Test_Views(TestCase):

    fixtures = [
        "list_data.json",
        "task_data.json",
        "sub_task_data.json"
    ]

    def setUp(self):
        self.client = Client()

    def test_07_get_all_lists(self):
        response = self.client.get(reverse('all_lists'))
        response_body = json.loads(response.content)
        self.assertEquals(response_body, all_lists)

    def test_08_get_all_tasks(self):
        list_id = 3  
        response = self.client.get(reverse('all_tasks', args=[list_id]))
        response_body = json.loads(response.content)
        self.assertEquals(response_body, all_tasks)
    
    def test_09_get_all_sub_tasks(self):
        list_id = 6
        task_id = 6
        response = self.client.get(reverse('all_sub_tasks', args=[list_id, task_id]))
        response_body = json.loads(response.content)
        self.assertEquals(response_body, all_sub_tasks)
        