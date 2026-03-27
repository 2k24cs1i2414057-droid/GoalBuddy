from django.urls import path
from .import views 

urlpatterns = [
    path("interview/",views.interview,name="interview"),
    path("feedback/",views.feedback,name="feedback")
]