from django.contrib import admin
from .models import Student, Roadmap

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'grade', 'stream', 'created_at']
    search_fields = ['user__username', 'user__email']

@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):
    list_display = ['title', 'student', 'goal', 'is_completed', 'created_at']
    search_fields = ['title', 'student__user__username']
    list_filter = ['is_completed']