from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    #path('ask-gemini/', views.generate_from_gemini , name =" ask_gemini"),
    #path('chat/', views.chat,name="Chat"),

]