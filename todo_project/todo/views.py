from django.shortcuts import render
from .models import Task

def home(request):
    queryset = Task.objects.all()
    return render(request,'todo/home.html',{'queryset': queryset})