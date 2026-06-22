from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.models import Student
from .models import Roadmap


@login_required(login_url="login")
def goal(request):
    if request.method == "POST":
        goal_name = request.POST.get("goal", "").strip()

        if not goal_name:
            messages.error(request, "Please choose a goal.")
            return redirect("goal")

        student, _ = Student.objects.get_or_create(
            user=request.user,
            defaults={"phone": ""}
        )

        roadmap = Roadmap.objects.filter(student=student).order_by("-created_at").first()

        if roadmap:
            roadmap.title = f"{goal_name} Roadmap"
            roadmap.goal = goal_name
            roadmap.description = f"Roadmap for {goal_name}"
            roadmap.is_completed = False
            roadmap.save()
        else:
            Roadmap.objects.create(
                student=student,
                title=f"{goal_name} Roadmap",
                goal=goal_name,
                description=f"Roadmap for {goal_name}",
            )

        messages.success(request, "Goal saved successfully.")
        return redirect("dashboard")

    return render(request, "goals/goal.html")