from django.urls import path

from myfirstapp.views import PersonListApiView
from . import apis

urlpatterns = [
    path('api/<int:pk>', apis.api.as_view(), name = "api"),
    path('get_person/', PersonListApiView.as_view()),
]

#  api/           http://127.0.0.1:8000/api/<DBの数字>   
#  get_person/    http://127.0.0.1:8000/get_person/