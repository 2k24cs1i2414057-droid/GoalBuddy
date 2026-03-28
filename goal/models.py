from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=True)
    grade = models.CharField(max_length=50, blank=True)
    stream = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Roadmap(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='roadmaps')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    goal = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

