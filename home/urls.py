from django.urls import path

from . import views

app_name = "home"

urlpatterns = [

    path('login', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),

    path('', views.Index.as_view(), name="index"),
    path('list/task/', views.ListTask.as_view(), name="list_task"),
    path('detail/task/<int:pk>/', views.DetailTask.as_view(), name="detail_task"),
    path('new/task/', views.CreateTask.as_view(), name="new_task"),
    path('update/task/<int:pk>/', views.UpdateTask.as_view(), name="update_task"),
    path('delete/task/<int:pk>/', views.DeleteTask.as_view(), name="delete_task"),
    
    path('list/service/', views.ListService.as_view(), name="list_service"),
    path('detail/service/<int:pk>/', views.DetailService.as_view(), name="detail_service"),
    path('new/service/', views.CreateService.as_view(), name="create_service"),
    path('update/service/<int:pk>/', views.UpdateService.as_view(), name="update_service"),
    path('delete/service/<int:pk>/', views.DeleteService.as_view(), name="delete_service"),
    

]