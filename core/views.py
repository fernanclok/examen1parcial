from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.models import User
#from django.dispatch import receiver
from core import forms
from core import models
from django.urls import reverse_lazy
#from django.contrib.auth import authenticate, login, logout



# class Login(generic.View):
#     template_name = "core/index.html"
#     context = {}
#     form_class = forms.LoginForm

#     def get(self, request):
#         self.context = {
#             "users": User.objects.all(),
#             "form": self.form_class
#         }
#         return render(request, self.template_name, self.context)
    
#     def post(self, request):
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             redirect("core:index")
#         return redirect("core:index")


# class Logout(generic.View):
#     def get(self, request):
#         logout(request)
#         return redirect("core:index")
    


# class SignUp(generic.CreateView):
#     template_name = "core/signup.html"
#     model = User
#     form_class = forms.SignupForm
#     success_url = reverse_lazy("core:index")

#     def form_valid(self, form):
#         form.save()
#         username = form.cleaned_data.get("username")
#         password1 = form.cleaned_data.get("password1")
#         user = authenticate(self.request, username=username, password=password1)
#         if user is not None:
#             login(self.request, user)
#         return redirect("core:index")




class Index(generic.View):
    template_name = "home/index.html"
    context = {}
    form_class = None

    def get(self, request):
        self.context = {
            "users": User.objects.all()
        }
        return render(request, self.template_name, self.context)

class ListTask(generic.View):
    template_name="core/list_task.html"
    context = {}

    def get(self, request):
        self.context = {
            "tasks":models.task.objects.all()
        }
        return render(request, self.template_name, self.context)



class DetailTask(generic.DetailView):
    template_name="core/details_task.html"
    model = models.task

class CreateTask(generic.CreateView):
    template_name = "core/create_task.html"
    model = models.task
    form_class = forms.NewTaskForm
    success_url = reverse_lazy("core:list_task")

class UpdateTask(generic.UpdateView):
    template_name = "core/update_task.html"
    model = models.task
    form_class = forms.UpdateTaskForm
    success_url = reverse_lazy("core:list_task")

class DeleteTask(generic.DeleteView):
    template_name = "core/delete_task.html"
    model = models.task
    success_url = reverse_lazy("core:list_task")





class ListService(generic.ListView):
    template_name="core/list_service.html"
    context_object_name = "services"
    queryset = models.service.objects.all

class DetailService(generic.DetailView):
    template_name="core/details_service.html"
    model = models.service

class CreateService(CreateView):
    template_name = "core/create_service.html"
    model = models.service
    form_class = forms.NewServiceForm
    success_url = reverse_lazy("core:list_service")

class UpdateService(generic.CreateView):
    template_name = "core/update_service.html"
    model = models.service
    form_class = forms.NewServiceForm
    success_url = reverse_lazy("core:list_service")

class DeleteService(generic.DeleteView):
    template_name = "core/delete_service.html"
    model = models.service
    success_url = reverse_lazy("core:list_service")