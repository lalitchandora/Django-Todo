from django.urls import path, include
from . import views 
urlpatterns = [
    path('',views.home,name="home"),
    path('delete/<int:id>',views.deletetask,name="delete"),
    path('edit/<int:id>',views.edittask,name="edit"),
    
]
