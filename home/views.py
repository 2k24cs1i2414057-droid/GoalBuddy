from django.shortcuts import render 

# Create your views here.

def home(request):
    return render(request, "home/home.html")

def parent(request):
    return render(request, "home/parent.html")

