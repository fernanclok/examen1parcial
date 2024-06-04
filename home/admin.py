from django.contrib import admin

# Register your models here.
from home import models

@admin.register(models.task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "user", "due_date", "progress", "status"]


@admin.register(models.service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["serv_name", "description", "type"]
