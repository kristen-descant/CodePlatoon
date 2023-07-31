from django.urls import path
from .views import All_Classes, A_Class

urlpatterns = [
    path('', All_Classes.as_view(), name='all_classes'),
    path('<str:id>', A_Class.as_view(), name='a_class')
]