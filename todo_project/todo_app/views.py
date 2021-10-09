from django.shortcuts import render
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
