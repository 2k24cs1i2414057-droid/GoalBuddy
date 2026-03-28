from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required(login_url='login')
def progress(request):
    return render(request, 'dashboard/progress.html')


@login_required(login_url='login')
def roadmap(request):
    return render(request, 'dashboard/roadmap.html')


@login_required(login_url='login')
def aichat(request):
    return render(request, 'dashboard/aichat.html')