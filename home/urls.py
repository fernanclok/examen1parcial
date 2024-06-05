
from django.urls import path
from django.contrib.auth.decorators import login_required
from home import views

app_name = "home"
urlpatterns = [
    path('homer/', login_required(views.Home.as_view()), name="homer"),
    path("", views.Index.as_view(), name = "index"),
    path('logout/', login_required(views.Logout.as_view()), name="logout"),
    # path('core/', include("core.urls"))
]