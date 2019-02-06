from uuid import uuid4

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from task.utils import yada_yada


class TaskQuerySet(models.QuerySet):
    def belongs_to(self, user):
        return self.filter(assignee=user)

    def is_open(self):
        return self.filter(is_complete=False)


class Task(models.Model):
    objects = TaskQuerySet.as_manager()

    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    description = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    due_at = models.DateTimeField(null=True, blank=True, verbose_name='Due')
    is_complete = models.BooleanField(default=False, verbose_name='Complete')
    is_archived = models.BooleanField(default=False, verbose_name='Archived')
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assignee')

    def __str__(self):
        return yada_yada(self.description)

    def get_absolute_url(self):
        return reverse('task-detail', args=(self.id, ))
