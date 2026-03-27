from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request,"dashboard/dashboard.html")

def progress(request):
    return render(request,"dashboard/progress.html")

def roadmap(request):
    return render(request,"dashboard/roadmap.html")  

def aichat(request):
    return render(request , "dashboard/aichat.html")
