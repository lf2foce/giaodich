from django.http.response import HttpResponseBase
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello, world!')


def greet(request, name):
    return render(request, 'hello/login.html', {'name': name})

def task(request):
    return render(request, 'hello/add.html')