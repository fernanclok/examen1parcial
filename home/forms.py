from django import forms
from core import models
from django.contrib.auth.forms import UserCreationForm
 # Asegúrate de importar correctamente tu modelo


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control"}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control"}))



class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Username"})) 
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Password"}))
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"Password"}))  
    first_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"First Name"})) 
    last_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Last Name"})) 
    email = forms.EmailField(max_length=32, widget=forms.EmailInput(attrs={"type":"text", "class":"form-control", "placeholder":"Email"})) 




