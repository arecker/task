from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from db import models


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        me = self.request.user
        return {
            'my_tasks': models.Task.objects.belongs_to(me).is_open()
        }


class TaskList(LoginRequiredMixin, ListView):
    model = models.Task


class TaskCreate(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('task-list')
    model = models.Task
    fields = [
        'description',
        'is_complete',
        'assignee',
        'due_at'
    ]
