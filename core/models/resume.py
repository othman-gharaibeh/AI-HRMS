from django.core.validators import FileExtensionValidator
from django.db import models

from .candidate import Candidate


class Resume(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="resumes",
    )
    file = models.FileField(
        upload_to="resumes/",
        validators=[FileExtensionValidator(["pdf", "docx", "txt"])],
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "core_resume"
        ordering = ["-uploaded_at", "-id"]

    def __str__(self):
        return f"Resume for {self.candidate.full_name}: {self.file.name}"
