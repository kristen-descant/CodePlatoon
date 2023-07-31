from django.db import models

# Create your models here.
class List(models.Model):
    list_name = models.CharField(default='My List', max_length=30)

    def __str__(self):
        return f'{self.list_name}'