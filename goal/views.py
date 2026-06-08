from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Student
from .models import Roadmap


@login_required(login_url='login')
def goal(request):

    if request.method == "POST":

        goal_name = request.POST.get("goal")

        student = Student.objects.get(user=request.user)

        Roadmap.objects.create(
            student=student,
            title=f"{goal_name} Roadmap",
            goal=goal_name,
            description=f"Roadmap for {goal_name}"
        )

        return redirect("dashboard")

    return render(request, "goals/goal.html")