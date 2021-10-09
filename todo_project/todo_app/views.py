from django.shortcuts import render, redirect
from .models import Todos
from .forms import ListForm


def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            todo_list = Todos.objects.all()
            return render(request, 'todo_app/index.html', {'todo_list': todo_list})
    else:
        todo_list = Todos.objects.all()
        return render(request, 'todo_app/index.html', {'todo_list': todo_list})


def about(request):
    return render(request, 'todo_app/about.html')


def create(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            todo_list = Todos.objects.all()
            return render(request, 'todo_app/create.html', {'todo_list': todo_list})
    else:
        todo_list = Todos.objects.all()
        return render(request, 'todo_app/create.html', {'todo_list': todo_list})


def delete(request, Todos_id):
    # çağrılan id yi getir ve sil
    selected_todo = Todos.objects.get(pk=Todos_id)
    selected_todo.delete()

    # silme işlemi sonrası gideceği sayfayı redirect ile belirtiriz
    return redirect('index')


def done(request, Todos_id):
    selected_todo = Todos.objects.get(pk=Todos_id)
    selected_todo.is_finished = False
    selected_todo.save()

    return redirect('index')


def undone(request, Todos_id):
    selected_todo = Todos.objects.get(pk=Todos_id)
    selected_todo.is_finished = True
    selected_todo.save()

    return redirect('index')


def update(request, Todos_id):
    if request.method == "POST":
        selected_todo = Todos.objects.get(pk=Todos_id)
        form = ListForm(request.POST or None, instance=selected_todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        selected_todo = Todos.objects.get(pk=Todos_id)
        return render(request, 'todo_app/update.html', {'selected_todo': selected_todo})

