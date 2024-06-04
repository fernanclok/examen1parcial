from django import forms
from home import models
from django.contrib.auth.forms import UserCreationForm

class NewTaskForm(forms.ModelForm):
    class Meta:
        model = models.task
        fields = [
            "title",
            "description",
            "user",
            "due_date",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el grantgoal description!"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "due_date": forms.NumberInput(attrs={"type":"number", "class":"form-control"}),
        }

class NewServiceForm(forms.ModelForm):
    class Meta:
        model = models.service
        fields = [
            "serv_name",
            "description",
            "type",
            
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal name!"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe la description de la tarea"}),
            "type": forms.Select(attrs={"type":"select", "class":"form-control"}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control"}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control"}))



class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Username"})) 
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Password"}))
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Password"}))  
    first_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"First Name"})) 
    last_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Last Name"})) 
    email = forms.EmailField(max_length=32, widget=forms.EmailInput(attrs={"type":"text", "class":"form-control", "placeholder":"Email"})) 




