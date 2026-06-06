from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def interview(request):
    return render(request , "interview/interview.html")

@login_required(login_url='login')
def feedback(request):
    return render(request , "interview/feedback.html") 