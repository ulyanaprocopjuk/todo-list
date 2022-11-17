from django.urls import path
from todoapp.views import *

urlpatterns = [
    path('', index, name="Home"),
    path('/addTask', addTask, name="Add Task"),
    path('/deleteTask/<int:id>', deleteTask, name="Delete Task"),
    path('/completedTask/<int:id>', completedTask, name="Task Completed"),
    path('/updateTask/<int:id>', updateTask, name="Update Task"),
    path('/deleteAllCompleted', deleteAllCompleted, name="Delete all Completed"),
    path('/deleteAll', deleteAll, name="Delete All"),
]
