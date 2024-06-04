from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.dispatch import receiver
from home import forms
from home import models
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout



class Login(generic.View):
    template_name = "home/index.html"
    context = {}
    form_class = forms.LoginForm

    def get(self, request):
        self.context = {
            "users": User.objects.all(),
            "form": self.form_class
        }
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #redirect("home:index")
        return redirect("home:index")


class Logout(generic.View):
    def get(self, request):
        logout(request)
        return redirect("home:index")
    


class SignUp(generic.CreateView):
    #template_name = "home/signup.html"
    model = User
    #form_class = SignupForm
    success_url = reverse_lazy("home:index")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password1)
        if user is not None:
            login(self.request, user)
        return redirect("home:index")




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
    success_url = reverse_lazy("home:list_task")

class UpdateTask(generic.CreateView):
    template = "home/create_task.html"
    model = models.task
    form_class = forms.NewTaskForm
    success_url = reverse_lazy("home:list_task")

class DeleteTask(generic.DeleteView):
    template = "home/create_task.html"
    model = models.task
    form_class = forms.NewTaskForm
    success_url = reverse_lazy("home:list_task")





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
    success_url = reverse_lazy("home:list_service")

class UpdateService(generic.CreateView):
    template = "home/update_service.html"
    model = models.task
    form_class = forms.NewTaskForm
    success_url = reverse_lazy("home:list_service")

class DeleteService(generic.DeleteView):
    template = "home/delete_service.html"
    model = models.task
    form_class = forms.NewTaskForm
    success_url = reverse_lazy("home:list_service")