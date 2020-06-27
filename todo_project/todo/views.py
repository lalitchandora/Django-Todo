from django.shortcuts import render, redirect
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
    return render(request,'todo/card.html',{'queryset': queryset,'form':form})

def deletetask(request,title):
    Task.objects.filter(title=title).delete()
    return redirect('home')