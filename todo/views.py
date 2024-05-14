from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Todo


class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"
    def get_queryset(self):
        status = self.request.GET.get('status')
        queryset = super().get_queryset()
        if status == 'completed':
            queryset = queryset.filter(status='completed')
        elif status == 'ongoing':
            queryset = queryset.filter(status='ongoing')
        return queryset
    def post(self, request, *args, **kwargs):
        if 'reset' in request.POST:
            return redirect(reverse_lazy('list'))
        return super().post(request, *args, **kwargs)


class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"


class TodoCreate(CreateView):
    model = Todo
    fields = ["title","description", "deadline"]
    success_url = reverse_lazy("list")
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['deadline'].widget = forms.DateInput(attrs={'class': 'datepicker'})
        return form

class TodoUpdate(UpdateView):
    model = Todo
    # status以外のフィールドを編集できるようにする
    fields = ["title","description", "deadline"]
    success_url = reverse_lazy("list")


class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")

# 完了ボタンを押したときの処理
class TodoComplete(UpdateView):
    model = Todo
    fields = ["status"]
    success_url = reverse_lazy("list")
    
    # template_name = "todo/todo_confirm_complete.html"

