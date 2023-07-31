from django.urls import path
from .views import All_Sub_Tasks

urlpatterns = [
    path('', All_Sub_Tasks.as_view(), name='all_sub_tasks')
]