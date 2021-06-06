from django.contrib import admin
from django.urls import path
from ToDoApp.views import todoView, addToDo, deleteToDo




app_name = "ToDoApp"

urlpatterns = [

	path('', todoView, name = "todo"),
	path('addtodo/', addToDo, name = "addtodo"),
	path('deletetodo/<int:todoId>/', deleteToDo, name = "deletetodo")

]