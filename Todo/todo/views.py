from django.shortcuts import render

from .models import Todo


# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/todo_list.html')


def todo_detail(request, pk):
    todo = Todo.objects.filter(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})
