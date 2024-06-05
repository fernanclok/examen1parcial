from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "core"

urlpatterns = [


    #login_required()
    path('list/task/', login_required(views.ListTask.as_view()), name="list_task"),
    path('detail/task/<int:pk>/', login_required(views.DetailTask.as_view()), name="detail_task"),
    path('new/task/', login_required(views.CreateTask.as_view()), name="new_task"),
    path('update/task/<int:pk>/', login_required(views.UpdateTask.as_view()), name="update_task"),
    path('delete/task/<int:pk>/', login_required(views.DeleteTask.as_view()), name="delete_task"),


    path('list/service/', login_required(views.ListService.as_view()), name="list_service"),
    path('detail/service/<int:pk>/', login_required(views.DetailService.as_view()), name="detail_service"),
    path('new/service/', login_required(views.CreateService.as_view()), name="create_service"),
    path('update/service/<int:pk>/', login_required(views.UpdateService.as_view()), name="update_service"),
    path('delete/service/<int:pk>/', login_required(views.DeleteService.as_view()), name="delete_service"),
    

]