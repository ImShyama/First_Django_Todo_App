from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    # return HttpResponse('hello, this is todo app.')
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
    {'all_items': all_todo_items})

def addTodo(request):
    # create a new toodo all_items
    new_item = TodoItem(content = request.POST['content'])
    # save
    new_item.save()
    # redirect the browser to '/todo/'
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')



    
    
    


