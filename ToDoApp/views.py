from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ToDoApp.models import ToDoItem

# Create your views here.


def todoView(request):
	# return HttpResponse("Hello this is from todoView in views.py") --> To inject simple content into the front page without using html template

	allTodoItems = ToDoItem.objects.all()
	todoList = {
		"content" : allTodoItems
	}
	
	return render(request, "ToDoApp/todo.html", context = todoList)


def addToDo(request):

	newContent = ToDoItem(content = request.POST['content'])
	newContent.save()

	return HttpResponseRedirect('/todo/')

def deleteToDo(request, todoId):
	deleteContent = ToDoItem.objects.get(id = todoId)
	deleteContent.delete()
	return HttpResponseRedirect('/todo/')

	


