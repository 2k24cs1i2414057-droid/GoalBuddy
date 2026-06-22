from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("progress/", views.progress, name="progress"),
    path("roadmap/", views.roadmap, name="roadmap"),
    path("aichat/", views.aichat, name="aichat"),
    path("chat-api/", views.chat_api, name="chat_api"),
]