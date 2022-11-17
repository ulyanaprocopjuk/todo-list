from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import *

from .forms import AddTaskForm


def index(request):
    tasks = Tasks.objects.all()
    form = AddTaskForm()
    return render(request, 'index.html', context={'tasks' : tasks, 'form' : form,})


def addTask(request):
    form = AddTaskForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')


def deleteTask(request, id):
    task = Tasks.objects.get(pk = id)
    task.delete()
    return redirect('/')


def completedTask(request, id):
    task = Tasks.objects.get(pk = id)
    task.completed = True
    task.save()
    return redirect('/')


def updateTask(request, id):
    task = Tasks.objects.get(pk = id)
    updateForm = AddTaskForm(instance=task)

    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'index.html', context={
                                                    'updateForm' : updateForm,
                                                    'key' : id,
                                                    'tasks' : Tasks.objects.all()
                                                 })


def deleteAllCompleted(request):
    completedTasks = Tasks.objects.filter(completed__exact=True).delete()
    return redirect('/')


def deleteAll(request):
    Tasks.objects.all().delete()
    return redirect('/')