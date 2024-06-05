from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
#from datetime import timedelta

# Create your models here.


CHOICES_TYPE = {
    "APP":"Aplicacion",
    "APPM":"Aplicacion movil",
    "SERV":"Servidores",
}

class service(models.Model):
    serv_name=models.CharField(max_length=64, default="Nombre del Servicio")
    description=models.CharField(max_length=255, default="Descripcion del Servicio")
    type=models.CharField(max_length=64, choices=CHOICES_TYPE)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.serv_name


class task(models.Model):
    title = models.CharField(max_length=64, default="New Task")
    service =  models.ForeignKey(service, on_delete=models.CASCADE)
    description = models.CharField(max_length=128, default="Task description")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    #due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    due_date = models.DateField( default=date.today, blank=True, null=False,)
    progress = models.FloatField(default=0.0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


