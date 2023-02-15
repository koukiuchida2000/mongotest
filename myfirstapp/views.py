"""

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# View関数を任意に定義
def index(request):
    return HttpResponse("Hello World")

"""
from django.shortcuts import render
from django.views.generic import ListView

from myfirstapp.models import SampleModel

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .renderers import PersonJSONRenderer
from .serializers import SampleSerializer

# Create your views here.

class PersonListApiView(ListAPIView):
    model = SampleModel # モデルを指定
    queryset = SampleModel.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (PersonJSONRenderer, ) # Rendererを指定
    serializer_class = SampleSerializer # Serializerを指定
