from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from todo.forms import TodoForm
from todo.models import Todo


class TodoList(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'


class TodoDetail(DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'


class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_create.html'


class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_update.html'


class TodoDelete(DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'
    success_url = reverse_lazy('todo_list_url')
