from django.shortcuts import render , redirect
from django.http import HttpResponse
from App.models import Task

# Create your views here.

def home(request): 
    task = Task.objects.filter(is_completed =False)
    context = {'task':task}
    return render(request , 'home.html', context)

def addtask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect ('home')