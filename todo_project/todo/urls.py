from django.urls import path, include
from . import views 
urlpatterns = [
    path('',views.home,name="home"),
    path('delete/<str:title>',views.deletetask,name="delete"),
    path('edit/<str:title>',views.edittask,name="edit"),
    
]
