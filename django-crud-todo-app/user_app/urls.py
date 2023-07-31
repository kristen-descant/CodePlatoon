from django.urls import path
from .views import Sign_Up, Log_In, Log_Out, User_Info, Master_Sign_Up

urlpatterns = [
    path('signup/', Sign_Up.as_view(), name='signup'),
    path('login/', Log_In.as_view(), name='login'),
    path('logout/', Log_Out.as_view(), name='logout'),
    path('', User_Info.as_view(), name='user_info'),
    path('master/', Master_Sign_Up.as_view(), name='master'),
]