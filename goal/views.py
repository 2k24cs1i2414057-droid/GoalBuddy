from django.shortcuts import render

# Create your views here.

def goal(request):
    return render(request , "goals/goal.html")