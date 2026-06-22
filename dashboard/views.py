import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from accounts.models import Student
from goal.models import Roadmap


def get_student_roadmap(user):
    student = Student.objects.filter(user=user).first()
    roadmap = Roadmap.objects.filter(student=student).order_by("-created_at").first() if student else None
    return student, roadmap


def mentor_reply(message, roadmap):
    text = message.lower()
    goal = roadmap.goal if roadmap else "your goal"

    if "roadmap" in text:
        return f"Your current goal is {goal}. Focus on foundation, daily practice, and weekly revision."
    if "schedule" in text or "study plan" in text:
        return f"For {goal}, do 2 hours concept study, 1 hour practice, and 30 minutes revision every day."
    if "weak" in text:
        return "Pick your weakest topic, solve 20 questions, note mistakes, and revise that same topic again at night."
    if "interview" in text:
        return "Practice self-introduction, strengths, weaknesses, and 3 goal-based answers daily."
    return f"I am your GoalBuddy mentor. For {goal}, stay consistent, review mistakes daily, and track progress weekly."


@login_required(login_url="login")
def dashboard(request):
    student, roadmap = get_student_roadmap(request.user)
    return render(request, "dashboard/dashboard.html", {"student": student, "roadmap": roadmap})


@login_required(login_url="login")
def progress(request):
    student, roadmap = get_student_roadmap(request.user)
    return render(request, "dashboard/progress.html", {"student": student, "roadmap": roadmap})


@login_required(login_url="login")
def roadmap(request):
    student, roadmap = get_student_roadmap(request.user)
    return render(request, "dashboard/roadmap.html", {"student": student, "roadmap": roadmap})


@login_required(login_url="login")
def aichat(request):
    student, roadmap = get_student_roadmap(request.user)
    return render(request, "dashboard/aichat.html", {"student": student, "roadmap": roadmap})


@require_POST
@login_required(login_url="login")
def chat_api(request):
    try:
        payload = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"reply": "Invalid request."}, status=400)

    message = payload.get("message", "").strip()
    if not message:
        return JsonResponse({"reply": "Please type a message first."}, status=400)

    _, roadmap = get_student_roadmap(request.user)
    return JsonResponse({"reply": mentor_reply(message, roadmap)})