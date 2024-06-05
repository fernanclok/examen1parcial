from django import forms
from core import models
from django.contrib.auth.forms import UserCreationForm


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = models.task
        fields = [
            "title",
            "service",
            "description",
            "user",
            "due_date",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe la nueva tarea"}),
            "service": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe la descripcion"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "due_date": forms.DateInput(attrs={'class': 'mi-clase', 'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = models.service.objects.all()  # Aquí asumimos que el modelo se llama Service

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
            "title": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe la nueva tarea"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe la descripcion"}),
            "user": forms.Select(attrs={"type":"select", "class":"form-control"}),
            "due_date": forms.DateInput(attrs={'class': 'mi-clase', 'type': 'date'}),
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
            "nombre": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nuevo servicio"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe la descripcion del servicio"}),
            "type": forms.Select(attrs={"type":"select", "class":"form-control"}),
        }

class UpdateServiceForm(forms.ModelForm):
    class Meta:
        model = models.service
        fields = [
            "serv_name",
            "description",
            "type",
            
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nuevo servicio"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe la descripcion del servicio"}),
            "type": forms.Select(attrs={"type":"select", "class":"form-control"}),
        }


