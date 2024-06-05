from django.shortcuts import render, redirect
from django.views import generic
#from django.views.generic import CreateView
from django.contrib.auth.models import User
#from django.dispatch import receiver
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm


class Home(generic.View):
    template_name = "home/Home.html"
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)


class Logout(generic.View):
    def get(self, request):
        logout(request)
        return redirect("home:index")
    


class SignUp(generic.CreateView):
    template_name = "home/signup.html"
    model = User
    form_class = SignupForm
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
    form_class = LoginForm

    # def get(self, request):
    #     self.context = {
    #         "users": User.objects.all()
    #     }
    #     return render(request, self.template_name, self.context)
    
    def get(self, request):
        self.context = {
            "users": User.objects.all(),
            "login_form": self.form_class
        }
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("core:list_task")
        else:
            return redirect("home:index")


