from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def list_task(request):
    tasks = Task.objects.all()
    return render(request, 'list_task.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
    return redirect('/tasks/')


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/tasks/')

def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task.title = title
        task.description = description
        task.save()
    return redirect('/tasks/')
    # return render(request, 'update_task.html', {'task': task})


