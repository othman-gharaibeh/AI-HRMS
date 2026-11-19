from django.contrib import admin

from .models import (
    Candidate,
    Department,
    InterviewQuestionSet,
    JobPosition,
    Resume,
    ScreeningResult,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name", "description"]
    list_filter = ["created_at"]


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ["title", "department", "created_at"]
    search_fields = ["title", "department__name", "description"]
    list_filter = ["department", "created_at"]


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone", "created_at"]
    search_fields = ["full_name", "email", "phone"]
    list_filter = ["created_at"]


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ["candidate", "file", "uploaded_at"]
    search_fields = ["candidate__full_name", "candidate__email", "file"]
    list_filter = ["uploaded_at"]


@admin.register(ScreeningResult)
class ScreeningResultAdmin(admin.ModelAdmin):
    list_display = ["candidate", "job_position", "score", "recommendation", "generated_at"]
    search_fields = ["candidate__full_name", "job_position__title", "summary"]
    list_filter = ["recommendation", "generated_at", "job_position"]


@admin.register(InterviewQuestionSet)
class InterviewQuestionSetAdmin(admin.ModelAdmin):
    list_display = ["candidate", "job_position", "screening_result", "generated_at"]
    search_fields = ["candidate__full_name", "job_position__title"]
    list_filter = ["generated_at", "job_position"]
