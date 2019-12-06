from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


# Create your views here.
def home_page(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {
        'todos': todos,
    })


def about_page(request):
    return render(request, 'todos/about.html', {})


def create_todo(request):
    title = request.POST['title']
    if len(title) > 4:
        Todo.objects.create(title=title)
    return redirect('todos:index')


def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.is_completed = True
    todo.save()
    return redirect('todos:index')


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todos:index')
