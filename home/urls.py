from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("parent/", views.parent, name="parent"),
    
]