from django.urls import path
from . import views 

urlpatterns = [
    path("goal/",views.goal, name="goal"),
]
