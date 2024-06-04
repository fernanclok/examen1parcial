from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('/list/task/<int:pk>/', views.ListTask.as_view(), name="list_task"),
    path('detail/task/<int:pk>/', views.DetailTask.as_view(), name="detail_task"),
    path('/new/task/<int:pk>/', views.CreateTask.as_view(), name="new_task"),
    path('/update/task/<int:pk>/', views.UpdateTask.as_view(), name="update_task"),
    path('/delete/task/<int:pk>/', views.DeleteTask.as_view(), name="delete_task"),
    
    path('/new/service/<int:pk>/', views.CreateService.as_view(), name="index"),
]