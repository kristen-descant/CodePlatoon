from django.db import models
from list_app.models import List

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(default='Task', max_length=30)
    completed = models.BooleanField(default=False)
    parent_list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.task_name}'
    