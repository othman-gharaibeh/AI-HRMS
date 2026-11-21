from django.urls import path

from .views import (
    candidate_create,
    department_create,
    interview_question_set_detail,
    job_position_create,
    resume_create,
    screening_result_detail,
)

urlpatterns = [
    path("departments/", department_create, name="department-create"),
    path("job-positions/", job_position_create, name="job-position-create"),
    path("candidates/", candidate_create, name="candidate-create"),
    path("resumes/", resume_create, name="resume-create"),
    path(
        "screening-results/<int:pk>/",
        screening_result_detail,
        name="screening-result-detail",
    ),
    path(
        "interview-questions/<int:pk>/",
        interview_question_set_detail,
        name="interview-question-set-detail",
    ),
]
