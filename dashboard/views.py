from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from goal.models import Roadmap
from accounts.models import Student
from django.views.decorators.csrf import csrf_exempt



@login_required(login_url='login')
def progress(request):
    return render(request, 'dashboard/progress.html')


@login_required(login_url='login')
def roadmap(request):
    return render(request, 'dashboard/roadmap.html')


@login_required(login_url='login')
def aichat(request):
    return render(request, 'dashboard/aichat.html')



@login_required(login_url='login')
def dashboard(request):

    student = Student.objects.filter(user=request.user).first()
    roadmap = None
    if student:
        roadmap = Roadmap.objects.filter(student=student).first()

    return render(request, 'dashboard/dashboard.html', {
        'roadmap': roadmap
    })
