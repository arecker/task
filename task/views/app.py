from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from db import models


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        me = self.request.user
        return {
            'my_tasks': models.Task.objects.belongs_to(me).is_open()
        }
