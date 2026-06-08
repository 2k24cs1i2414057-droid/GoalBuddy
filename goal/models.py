from django.db import models
from accounts.models import Student

class Roadmap(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='roadmaps'
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    goal = models.CharField(max_length=200)

    is_completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title