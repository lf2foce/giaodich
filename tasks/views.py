from django.shortcuts import render
from django import forms
# Create your views here.


tasks = ['Toa', 'cam', 'chuoi']

class NewTaskForm(forms.Form):
    task = forms.CharField(label='new task', max_length=50)
    priority = forms.IntegerField(label='priority', min_value=1, max_value=3)

def index(request):
    return render(request, 'tasks/index.html', {'tasks': tasks})

def add(request):
    return render(request, 'tasks/add.html', {'form': NewTaskForm()})
