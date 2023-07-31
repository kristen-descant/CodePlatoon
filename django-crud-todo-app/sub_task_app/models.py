from django.db import models
from task_app.models import Task

# Create your models here.
class Sub_Task(models.Model):
    sub_task_name = models.CharField(default='Sub Task', max_length=30)
    completed = models.BooleanField(default=False)
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sub_task_name}'