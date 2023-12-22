from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home , name= 'home'),
    
    # add task
    path ('todo/', views.addtask , name= 'addtask'),
    
    # mark as done
    path ('done/<int:pk>/', views.done , name='done'),

    # mark as done
    path ('undone/<int:pk>/', views.undone , name="undone"),

    #edit feature
    path ('edit/<int:pk>/', views.edit , name="edit"),

    #delete Task
    path ('delete/<int:pk>/', views.delete , name="delete")
]
