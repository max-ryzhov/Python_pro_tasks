from django.http import HttpResponse


def index(request):
    return HttpResponse("Любой текст")

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]

