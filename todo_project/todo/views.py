from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import CreateTaskForm

def home(request):
    if request.method=="POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateTaskForm()
    queryset = Task.objects.all()[::-1]
    context = {
        'queryset': queryset,
        'form': form,
        'url': 'home'
    }
    return render(request,'todo/card.html', context)

def deletetask(request,title):
    Task.objects.filter(title=title).delete()
    return redirect('home')


def edittask(request,title):
    task = get_object_or_404(Task,title=title)
    if request.method=="POST":
        form = CreateTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateTaskForm(instance=task)
    return render(request,'todo/edit.html',{'form':form})
    