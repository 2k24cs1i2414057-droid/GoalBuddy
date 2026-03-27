from django.db import models

# Create your models here.

from django.db import models

# Student Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Roadmap Model
class Roadmap(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='roadmaps')
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title