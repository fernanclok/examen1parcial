from django import forms
from core import models
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

class UpdateTaskForm(forms.ModelForm):
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


