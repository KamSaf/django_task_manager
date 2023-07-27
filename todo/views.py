from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.models import User
from datetime import datetime
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


def about(request):
    return render(request, 'todo/about.html')


def welcome(request):
    return render(request, 'todo/welcome.html')


def contact(request):
    return render(request, 'todo/contact.html')


def create_todo(request, username):
    if request.user.is_authenticated and request.user.username == username:
        Todo.objects.create(title=request.POST.get('title'),
                            date_added=datetime.now(),
                            author=request.user)
    else:
        messages.error(request, 'You need to be logged in to add item 🧐')
    return redirect('users_todos', username=username)


def delete_todo(request, pk):
    todo = Todo.objects.filter(id=pk).first()
    if request.user.is_authenticated and request.user == todo.author:
        todo.delete()
    else:
        messages.error(request, 'You have no permission to delete this item 🧐')
    return redirect('users_todos', username=request.user.username)


def update_status(request, pk):
    todo = Todo.objects.filter(id=pk).first()
    if request.user.is_authenticated and request.user == todo.author:
        todo.status = not todo.status
        todo.save()
    else:
        messages.error(request, 'You have no permission to edit this item 🧐')
    return redirect('users_todos', username=request.user.username)


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo/home.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        if self.request.user == user:
            return Todo.objects.filter(author=user)
        raise PermissionError
