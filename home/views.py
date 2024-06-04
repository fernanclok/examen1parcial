from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.dispatch import receiver
from home import forms
from home import models
from django.urls import reverse_lazy


# Create your views here.

class Index(generic.View):
    template_name = "home/index.html"
    context = {}
    form_class = None

    def get(self, request):
        self.context = {
            "users": User.objects.all()
        }
        return render(request, self.template_name, self.context)

class ListTask(generic.ListView):
    template_name="home/list_task.html"
    queryset = models.task.objects.all


class DetailTask(generic.DetailView):
    template_name="home/details_task.html"
    model = models.task

class CreateTask(generic.CreateView):
    template = "home/create_task.html"
    model = models.task
    form_class = forms.NewTaskForm
    #success_url = reverse_lazy("home:list_task")

class UpdateTask(generic.CreateView):
    template = "home/create_task.html"
    model = models.task
    form_class = forms.NewTaskForm
    #success_url = reverse_lazy("home:list_task")

class DeleteTask(generic.DeleteView):
    template = "home/create_task.html"
    model = models.task
    form_class = forms.NewTaskForm
    #success_url = reverse_lazy("home:list_task")





class ListService(generic.ListView):
    template_name="home/list_service.html"
    queryset = models.task.objects.all


class DetailService(generic.DetailView):
    template_name="home/details_service.html"
    model = models.task

class CreateService(generic.CreateView):
    template = "home/create_service.html"
    model = models.task
    form_class = forms.NewTaskForm
    #success_url = reverse_lazy("home:list_task")

class UpdateService(generic.CreateView):
    template = "home/create_service.html"
    model = models.task
    form_class = forms.NewTaskForm
    #success_url = reverse_lazy("home:list_task")

class DeleteService(generic.DeleteView):
    template = "home/create_service.html"
    model = models.task
    form_class = forms.NewTaskForm
    #success_url = reverse_lazy("home:list_task")