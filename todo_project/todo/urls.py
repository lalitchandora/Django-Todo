from django.urls import path, include
from . import views 
urlpatterns = [
    path('',views.home,name="home"),
    path('delete/<str:title>',views.deletetask,name="delete"),
    #path('create/<str:task_title>/<str:task_text>',views.createtask,name="create"),
    
]
